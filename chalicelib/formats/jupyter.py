import nbformat
from nbconvert import HTMLExporter

def render(content):
    nb = nbformat.reads(content, as_version=4)
    html_exporter = HTMLExporter()
    html_exporter.template_file = 'basic'
    (body, resources) = html_exporter.from_notebook_node(nb)
    # TODO: extract the images and store them separately
    return body


