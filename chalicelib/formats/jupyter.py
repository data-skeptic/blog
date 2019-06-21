import nbformat
from nbconvert import HTMLExporter
from traitlets.config import Config
from .. import renderer

def remove_tag(s, tag_name, class_name):
	s2 = s
	open_tag = f"<{tag_name}"
	close_tag = f"</{tag_name}>"
	i = s2.find(open_tag)
	while i != -1:
		j = s2.find('>', i)
		check = s2.find(f"class='{class_name}'", i)
		if check == -1:
			check = s2.find(f'class="{class_name}"', i)
		k = s2.find(close_tag, i)
		if check > i and check < k:
			if k == -1:
				return s2
			s2 = s2[0:j+1] + s2[k:]
		i = s2.find(open_tag, i+1)
	return s2


def render(content):
	c = Config()
	c.HTMLExporter.preprocessors = ['nbconvert.preprocessors.ExtractOutputPreprocessor']
	html_exporter = HTMLExporter(config=c)
	html_exporter.preprocessors
	s = content
	notebook = nbformat.reads(s, as_version=4)
	notebook.cells[0]
	html, x = html_exporter.from_notebook_node(notebook)
	#print(x.keys())
	#(['metadata', 'output_extension', 'inlining', 'outputs', 'raw_mimetypes', 'global_content_filter'])
	for output in x['outputs'].keys():
		data = x['outputs'][output]
		f = open(output, 'wb')
		f.write(data)
		f.close()

	i = html.find("<body>") + 6
	j = html.find("</body>")
	html = renderer.fix_string_for_db(html[i:j])
	html = remove_tag(html, 'a', 'anchor-link')
	html = remove_tag(html, 'div', 'prompt input_prompt')
	return html
