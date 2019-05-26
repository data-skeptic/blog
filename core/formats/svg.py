import os
from urllib.parse import quote

def render(content, s3, bucket_name, prefix):
    i = 0
    ranges = []
    while i < len(content):
        i = next_delimiter(content, i, False)
        if i != -1:
            j = next_delimiter(content, i+1, True)
            if j != -1:
                ranges.append([i, j+1])
        if i == -1 or j == -1:
            i = len(content)
        else:
            i = j + 1
    print("Found " + str(len(ranges)) + " latex statements to render.")
    updated_contents = replace_latex_with_svgs(s3, ranges, content, bucket_name, prefix)
    return updated_contents


def next_delimiter(s, a, is_closing, delim='$'):
    i = s.find(delim, a)
    if i > 0:
        check_for_preceeding_whitespace = s[i-1:i]
        if not(is_closing) and not(check_for_preceeding_whitespace.isspace()) and not(check_for_preceeding_whitespace==">"):
            return next_delimiter(s, is_closing, i+1)
        if contained_in_tag(s, i, "code"): # For R stuff
            return next_delimiter(s, is_closing, i+1)
        if contained_in_tag(s, i, "pre"):  # For R stuff
            return next_delimiter(s, is_closing, i+1)
    if i == -1:
        return -1
    if i > 0:
        before = s[i-1]
        if before == '\\':
            return next_delimiter(s, is_closing, a+1)
    return i


def replace_latex_with_svgs(s3, ranges, contents, bucket_name, prefix):
    # Go backwards because this is destructive of the source
    # Backwards makes debugging easier
    i = len(ranges) - 1
    while i >= 0:
        r = ranges[i]
        b = r[0]
        e = r[1]
        latex = contents[b+1:e-1]
        m = len(latex)
        if m > 1000:
            print("Latex string is too long, probably an error if parsing")
            sys.exit(-1)
        if m > 100:
            m = 100
        print('latex raw:', latex[0:m])
        if type(latex) != str:
            latex = latex.decode('utf-8')
        latex = latex.replace('&amp;', '&')
        latex = latex.replace('&lt;', '<')
        latex = latex.replace('&gt;', '>')
        blatex = latex
        fname = escape_latex(latex)
        fname = fname + ".svg"
        s3key =  f"{prefix}/" + fname
        objs = list(s3.Bucket(bucket_name).objects.filter(Prefix=s3key))
        # TODO: don't re-create
        fnn = quote(fname).replace('%20', '+')
        svguri = "http://s3.amazonaws.com/" + bucket_name + "/" + f"{prefix}/" + fnn
        render_and_upload_latex(s3, latex, fname, bucket_name, s3key)
        imgTag = "<img className='latex-svg' src='" + svguri + "' alt='" + blatex + "' />"
        if type(contents) != str:
            contents = contents.decode('utf-8')
        contents = contents[0:b] + imgTag + contents[e:len(contents)]
        i -= 1
    #
    return contents


def render_and_upload_latex(s3, latex, fname, bucket_name, s3key):
    cmd = '/usr/local/lib/node_modules/mathjax-node/bin/tex2svg '
    cmd += '"' + latex + '"'
    rendered = os.popen(cmd).read()
    f = open(fname, 'w')
    f.write(rendered)
    f.close()
    f = open(fname, 'rb')
    fake_handle = f
    fname = fname.encode('utf-8')
    res = s3.Bucket(bucket_name).put_object(Key=s3key, Body=fake_handle, ContentType='image/svg+xml', ACL='public-read')
    os.remove(fname)



def contained_in_tag(s, pos, tag):
    stag = "<" + tag.lower() + ""
    etag = "</" + tag.lower() + ">"
    before = s[0:pos].lower()
    after  = s[pos:].lower()
    i = before.rfind(stag)
    if i == -1:
        return False
    i2 = before.rfind(etag)
    if i2 != -1 and i < i2:
        return False
    j = after.find(etag)
    if j == -1:
        return False
    j2 = after.find(stag)
    if j2 < j:
        return False
    return True


def escape_latex(latex):
    fname = latex.replace("\\", "\\\\") \
    .replace(":", "%3A") \
    .replace(";", "%3B") \
    .replace('"', '\"') \
    .replace("|", "\\|") \
    .replace("<", "%3C") \
    .replace(">", "%3E") \
    .replace("*", "%2A") \
    .replace("=", "%3D") \
    .replace("+", "%2B") \
    .replace("?", "%3F") \
    .replace("/", "%2F")
    if fname.startswith('\\'):
        fname = 'l_' + fname
    return fname



