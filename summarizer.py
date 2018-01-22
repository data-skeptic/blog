import sys
import re
import bs4 as soup
import string
from parsers import parsers


def get_desc(contents):
    """Accepts a string in html format; returns a description"""
    lcontents = contents.lower()
    i = lcontents.find('<p>')
    if i != -1:
        j = lcontents.find('</p>', i)
        desc = contents[i+3:j-4]
        desc = re.sub('<[^<]+?>', '', desc)
    else:
        desc = ''
    if len(desc) > 0:
        if desc[-1] == '<':
            desc = desc[:-1]
    return desc


def get_title(absfilename, contents):
    """Accepts a filename AND it's contents; returns a title"""
    lcontents = contents.lower()
    c = 1
    b = soup.BeautifulSoup(contents, "lxml")
    while c < 6:
        tag = b.find('h' + str(c))
        if tag != None:
            return tag.text.replace('&#182;', '')
        c += 1
    i = absfilename.rfind('/')
    j = absfilename.rfind('.')
    fname = absfilename[i+1:j]
    fname = fname.replace('-', ' ').replace('_', ' ')
    fname = fname.title()
    return fname


def get_pretty_name(absfilename, title):
    """Given source file and title, select SEO friendly name"""
    i = absfilename.rfind('/')
    if absfilename[i+1:].lower() == 'readme.htm':
        return '/' + absfilename[0:i+1]
    pn = title.lower().replace(' ', '-')
    valid_chars = "-_.() %s%s" % (string.ascii_letters, string.digits)
    pn2 = ''.join(c for c in pn if c in valid_chars)
    i = absfilename.rfind('/')
    return '/' + absfilename[0:i] + '/' + pn2


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("USAGE: python3 summarizer.py path/to/src/file/filename.md")
    else:
        absfilename = sys.argv[1]
        i = absfilename.rfind('.')
        if i != -1:
            ext = absfilename[i:]
            if ext in parsers:
                parser = parsers[ext]
                contents = parser(absfilename)
                desc = get_desc(contents)
                title = get_title(absfilename, contents)
                print(title)
                s = ""
                for i in range(len(title)):
                    s += "="
                print(s)
                print(desc)
            else:
                print("No parser for extension of " + ext)
        else:
            print("Filename needs to end in .ipynb, .md, or .Rhtml")
