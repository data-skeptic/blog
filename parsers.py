import markdown
import rpy2.robjects as robjects
from nbconvert import HTMLExporter

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
        c = c.replace('\x91', '`')
        c = c.replace('\x92', '\'')
        c = c.replace('\x93', '"')
        c = c.replace('\x94', '"')
        c = c.replace('\x96', '-')
        c = c.replace('\x97', '-')
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
    print(reval)
    print(type(reval))
    r2 = robjects.reval(reval)
    fname = r2[0]
    f = open(fname, 'r')
    c = f.read()
    f.close()
    return c

parsers = {
    '.md': md,
    '.Rmd': knitr,
    '.Rhtml': knitr,
    '.ipynb': nbconverter
}