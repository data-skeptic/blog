
def get_blogs():
    bucket_name = 'dataskeptic.com'
    database = dao.get_database(s3, bucket_name, db_s3_key)
    return database


def process_commit(database, s3, bucket_name, repo, branch, commit):
    author = commit['author']['email']
    for filepath in commit['added']:
        renderer.render_one(database, s3, bucket_name, repo, branch, filepath, author)
        publish()
    for filepath in commit['removed']:
        doc_type = renderer.get_type(filepath)
        renderer.remove(s3, bucket_name, database, doc_type, filepath)
        dao.remove(filepath)
    for filepath in commit['modified']:
        renderer.render_one(database, s3, bucket_name, repo, branch, filepath, author)


def update_attributes(url, attribute, value):
    bucket_name = 'dataskeptic.com'
    database = dao.get_database(s3, bucket_name, db_s3_key)
    if url not in database:
        raise Exception("No record of {url}".format(url=url))
    old_record = database[url]
    new_record = json.loads(json.dumps(old_record))
    if value is None and attribute in new_record:
        del new_record[attribute]
    else:
        new_record[attribute] = value
    database[url] = new_record
    dao.update_database(s3, bucket_name, db_s3_key, database)
    # TODO: add to elastic search
    #blog_content =
    #elastic.add(database, url, blog_content)
    return {"old_record": old_record, "new_record": new_record}


def get_attribute(s3, bucket_name, db_s3_key, url, attribute):
    database = dao.get_database(s3, bucket_name, db_s3_key)
    if url not in database:
        raise Exception("No record of {url}".format(url=url))
    return database[url]


