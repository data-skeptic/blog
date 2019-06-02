import markdown

def render(content):
    html = markdown.markdown(content, extensions=['markdown.extensions.tables'])
    return html
