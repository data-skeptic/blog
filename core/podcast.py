import botocore
import pandas as pd
import xmltodict
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
            print(record)
            database[record['url']] = record
        return database
        

def update_podcast_rss(s3, bucket_name, db_s3_key, url):
    r = requests.get(url)
    f = open(fname, 'wb')
    f.write(r.text.encode
        ('utf-8'))
    f.close()
    get_database(s3, bucket_name, db_s3_key, prefix="blog/")
    updated = update_podcast_from_file(s3, database, fname)
    if updated:
        print("Podcast updates made")
        update_database(s3, bucket_name, db_s3_key, database)


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


def update_podcast_from_file(s3, database, fname):
    updated = False
    with open(fname) as fd:
        xml = xmltodict.parse(fd.read())
        episodes = xml['rss']['channel']['item']
        n = len(episodes)
        print(f'Number of episodes: {n}')
        for episode in episodes:
            result = update_episode(database, episode)
            updated = updated | result
    return updated


def requires_update(ep, guid, duration):
    if 'guid' not in ep:
        return True
    if duration not in ep:
        return True
    if ep['guid'] != guid:
        return True
    if ep['duration'] != duration:
        return True
    return False


def update_episode(database, episode):
    updated = False
    guid = episode['guid']['#text']
    url = episode['enclosure']['@url']
    link = episode['link']
    duration = episode['itunes:duration'] # format: 03:56
    prettyname = link.replace("https://dataskeptic.com", "")
    if prettyname in database:
        ep = database[prettyname]
        if requires_update(ep, guid, duration):
            ep['duration'] = duration
            ep['guid'] = guid
            # TODO: related content (media, guest, etc)
            # TODO: guid
            database[prettyname] = ep
            return True
    else:
        # TODO: if episode is more than N minutes old, email Kyle once
        return False

