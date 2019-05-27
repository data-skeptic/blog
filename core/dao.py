import botocore
import pandas as pd

from . import renderer

def get_database(s3, bucket_name, db_s3_key, prefix="blog/"):
    obj = s3.Object(bucket_name, db_s3_key)
    try:
        content = obj.get()['Body'].read()
        fn = 'temp.parquet'
        f = open(fn, 'wb')
        f.write(content)
        f.close()
        df = pd.read_parquet(fn)
        df.reset_index(inplace=True)
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


def initialize_database(s3, bucket_name, prefix):
    print("Initializing database")
    # TODO: crawl and make first parquet file
    objs = list(s3.Bucket(bucket_name).objects.filter(Prefix=prefix))
    if len(objs) == 0:
        return {}
    else:
        print(f"Found {len(objs)} existing blog posts to import.")
        database = {}
        for obj in objs:
            # TODO: render it and add it to the database
            s3key = obj.key
            obj2 = s3.Object(bucket_name, s3key)
            content = obj2.get()['Body'].read().decode('utf-8')
            author = ""
            record = renderer.generate_metadata(s3key, content, author)
            database[record['url']] = record
        return database


def update_database(s3, bucket_name, db_s3_key, database):
    print("save db")
    records = list(database.values())
    df = pd.DataFrame(records)
    df.set_index('url', inplace=True)
    fn = 'temp.parquet'
    df.to_parquet(fn)
    f = open(fn, 'rb')
    content = f.read()
    f.close()
    obj = s3.Object(bucket_name, db_s3_key)
    obj.put(Body=content)


