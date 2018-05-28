import markdown
import os
import shutil
import base64
import rpy2.robjects as robjects
from nbconvert import HTMLExporter
from contextlib import contextmanager
import sys, os

@contextmanager
def suppress_stdout():
    with open(os.devnull, "w") as devnull:
        old_stdout = sys.stdout
        sys.stdout = devnull
        try:  
            yield
        finally:
            sys.stdout = old_stdout

def md(absfile):
    try:
        f = open(absfile, 'r')
        c = f.read()
        f.close()
    except UnicodeDecodeError:
        f = open(absfile, 'rb')
        c = f.read()
        f.close()
        formats = ["utf-8", "cp1252"]
        done = False
        for fmt in formats:
            if not(done):
                try:
                    c = c.decode(fmt)
                    done = True
                except UnicodeDecodeError:
                    pass
    if type(c) == str:
        c = c.replace('\xe2\x80\x9c', '"')
        c = c.replace('\xe2\x80\x99', "'")
        c = c.replace('\xe2\x80\x9d', '"')
        c = c.replace('\xe2\x80\x93', "-")
        c = c.replace('\xe2\x80\x98', "'")
        c = c.replace('\xe2\x80\x94', "-")
        c = c.replace('\x92', '\'')
        c = c.replace('\x93', '"')
        c = c.replace('\x94', '"')
        c = c.replace('\x96', '-')
        c = c.replace('\x97', '-')
    i = c.find('```')
    while i != -1:
        j = c.find('```', i+3)
        if j != -1:
            c = c[0:i] + '<code><pre>' + c[i+3:j] + '</pre></code>' + c[j+3:]
            i = c.find('```', j+3)
        else:
            i = -1
    html = markdown.markdown(c, extensions=['markdown.extensions.tables'])
    return html


def nbconverter(absfile):
    f = open(absfile, 'r')
    c = f.read()
    f.close()
    nb = nbformat.reads(c, as_version=4)
    html_exporter = HTMLExporter()
    html_exporter.template_file = 'basic'
    (body, resources) = html_exporter.from_notebook_node(nb)
    return body


def knitr(absfile):
    i = absfile.rindex('/')
    j = absfile.find('.', i)
    s = absfile[0:j]
    figpath = s + '_img/'
    reval = """
        knitr::opts_chunk$set(echo=FALSE, fig.path='{figpath}')
        library('knitr')
        knit('{absfile}')
        """.format(figpath=figpath, absfile=absfile)
    print('--------------------------------------')
    #print(reval)
    #print(type(reval))
    with suppress_stdout():
        r2 = robjects.reval(reval)
    fname = r2[0]
    f = open(fname, 'r')
    c = f.read()
    f.close()
    if c[0:3] == '---':
        j = c.find('---', 4)
        c = c[j+3:]
    fn = 'tmp.md'
    f = open(fn, 'w')
    f.write(c)
    f.close()
    c = md(fn)
    #TODO: Remove header part
    #TODO: handle markdown
    #TODO: upload images
    return c


def html_parser(absfile):
    last_slash = absfile.rfind('/') + 1
    dname = absfile[0:last_slash]
    inputFile = absfile[last_slash:]
    if dname[-1] != "/":
        dname += "/"
    x = inputFile.rfind('.')
    outputDirForImages = dname + "src-" + inputFile[0:x]
    # TODO: remove script
    rendered_content_as_string = extract_images_save_locally(dname, inputFile, outputDirForImages)
    rendered_content_as_string2 = remove_script_tags(rendered_content_as_string)
    rendered_content_as_string2 = remove_remaining_elements_tags(rendered_content_as_string2)
    return rendered_content_as_string2


def remove_remaining_elements_tags(content):
    content_lower = content.lower()
    i = content_lower.find("<body")
    if i != -1:
        j = content_lower.find(">", i)
        content = content[j+1:]
        i = content_lower.find("</body", j+1)
        content = content[:i]
    return content


def remove_script_tags(content):
    content_lower = content.lower()
    i = content_lower.find("<script")
    if i != -1:
        j = content_lower.find("</script>", i)
        if j == -1:
            print("ERROR: unclosed <script> tag")
            sys.exit(-1)
        content2 = content[0:i] + content[j + 9:]
        return remove_script_tags(content2)
    return content


def extract_images_save_locally(dname, inputFile, outputDirForImages):
    if outputDirForImages[-1] != "/":
        outputDirForImages += "/"
    absOutputDirForImages = outputDirForImages
    if os.path.exists(absOutputDirForImages):
        shutil.rmtree(absOutputDirForImages)
    os.makedirs(absOutputDirForImages)
    f = open(dname + inputFile, 'r')
    s = f.read()
    f.close()
    s_lower = s.lower()
    i = -1
    i = s_lower.find('src="data:image/', i+1)
    c = 0
    replacements = []
    while i > 0:
        j = s_lower.find('"', i+5)
        k = s_lower.find("image/", i)
        m = s_lower.find(";", k)
        n = s_lower.find(",", m)
        b64s = s[n+1:j]
        z = len(b64s) - 10
        #try:
        if 1==1:
            base64encoding = base64.b64decode(b64s)
            typ = s[k+6:m]
            fname = outputDirForImages + "img_" + str(c) + '.' + typ
            f = open(fname, 'wb')
            f.write(base64encoding)
            f.close()
            relative_filename = "/blog/" + fname
            replacement = {"start": i+5, "end": j, "replacement": relative_filename}
        try:
            replacements.append(replacement)
        except:
            print("Error on ", c)
        i = s_lower.find('src="data:image/', i+1)
        c += 1

    for r in range(len(replacements)):
        replacement = replacements[len(replacements)-r-1]
        start = replacement['start']
        end = replacement['end']
        fname = replacement['replacement']
        s = s[0:start] + fname + s[end:]
    return s


parsers = {
    '.md': md,
    '.Rmd': knitr,
    '.Rhtml': knitr,
    '.ipynb': nbconverter,
    '.htm': html_parser,
    '.html': html_parser
}