import markdown
import sys

absfile = sys.argv[1]

f = open(absfile, 'r')
c = f.read()
f.close()
c = c.replace('\x97', '-')
c = unicode(c, 'utf-8')
html = markdown.markdown(c)
print(html)