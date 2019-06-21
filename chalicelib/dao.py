import botocore
import pandas as pd
import time
import json

from . import renderer

def initialize_database(s3, bucket_name, prefix):
    print("Initializing database")
    objs = list(s3.Bucket(bucket_name).objects.filter(Prefix=prefix))
    if len(objs) == 0:
        return {}
    else:
        n = len(objs)
        print("Found {n} existing blog posts to import.".format(n=n))
        database = {}
        for obj in objs:
            s3key = obj.key
            obj2 = s3.Object(bucket_name, s3key)
            content = obj2.get()['Body'].read().decode('utf-8')
            author = ""
            record = renderer.generate_metadata(s3key, content, author)
            database[record['url']] = record
        return database


def get_database(s3, bucket_name, db_s3_key, prefix="blog/"):
    obj = s3.Object(bucket_name, db_s3_key)
    try:
        content = obj.get()['Body'].read()
        fn = 'temp.parquet'
        f = open(fn, 'wb')
        f.write(content)
        f.close()
        df = pd.read_parquet(fn)
        #print(df)
        #df.reset_index(inplace=True)
        df.fillna('', inplace=True)
        df.rename(columns={'index': 'url'}, inplace=True)
        database = {}
        for r in range(df.shape[0]):
            row = df.iloc[r]
            url = row['url']
            database[url] = row.to_dict()
        return database
    except botocore.exceptions.ClientError as e:
        if e.response['Error']['Code'] == "404" or e.response['Error']['Code'] == "NoSuchKey":
            return initialize_database(s3, bucket_name, prefix)
        else:
            print(e.response['Error']['Code'])
            print(e)
            raise e


def update_database(s3, bucket_name, db_s3_key, database):
    print("save db")
    ts = int(time.time())
    backup_key = db_s3_key.replace(".parquet", ".{ts}.parquet".format(ts=ts))
    #s3.Object(bucket_name, backup_key).copy_from(CopySource='{bucket_name}/{db_s3_key}'.format(bucket_name=bucket_name, db_s3_key=db_s3_key))
    # TODO: copy the old one with a TTL as a backup
    fn = 'temp.parquet'
    df = pd.DataFrame(database)
    df.to_parquet(fn)
    f = open(fn, 'rb')
    content = f.read()
    f.close()
    obj = s3.Object(bucket_name, db_s3_key)
    obj.put(Body=content)
    obj = s3.Object(bucket_name, db_s3_key.replace(".parquet", ".json"))
    jdict = {}
    for r in range(df.shape[0]):
        row = df.iloc[r]
        url = row.name
        jdict[url] = row.to_dict()
    obj.put(Body=json.dumps(jdict))


def remove(filepath):
    dao.remove(filepath)
    elastic.remove(url)
    # TODO: remove from parquet database

