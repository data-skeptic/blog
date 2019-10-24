
@app.route("/blog/posts", methods=['GET'])
def blog_posts():
    params = app.current_request.query_params
    print(params)
    blogs = blog.get_blogs()
    if params is not None and 'id' in params:
        url = params['id']
        print(url)
        # TODO: prefix matching
        return blogs[url]
    else:
        return blogs


@app.route("/blog/deploy", methods=['POST'], content_types=['application/x-www-form-urlencoded'])
def blog_deploy():
    payloadstr = app.current_request.raw_body.decode('utf-8')
    print(payloadstr)
    prefix = 'payload='
    if payloadstr.find(prefix) == 0:
        payloadstr = payloadstr[len(prefix):]
    payload = unquote(payloadstr)
    event = json.loads(payload)
    return blog.handle_update(event)


@app.route("/blog/posts/update", methods=['POST'])
def blog_posts_update():
    o = app.current_request.json_body
    url = o['url']
    attribute = o['attribute']
    value = o['value']
    return blog.update_attributes(url, attribute, value)


@app.route("/blog/podcast/update", methods=['POST'])
def update_podcast():
    url = 'http://dataskeptic.libsyn.com/rss'
    bucket_name = 'dataskeptic.com'
    db_s3_key = 'posts.db.csv'
    database = dao.get_database(s3, bucket_name, db_s3_key)
    print('fetching {url}'.format(url=url))
    podcast.update_podcast_rss(database, s3, bucket_name, db_s3_key, url)


@app.schedule(Rate(1, unit=Rate.MINUTES))
def scheduled(event):
    url = 'http://dataskeptic.libsyn.com/rss'
    print('fetching {url}'.format(url=url))
    print(event)
    bucket_name = 'dataskeptic.com'
    db_s3_key = 'posts.db.csv'
    database = dao.get_database(s3, bucket_name, db_s3_key)
    podcast.update_podcast_rss(database, s3, bucket_name, db_s3_key, url)
