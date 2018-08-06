# -*- coding: utf-8 -*-
DESCRIPTION = (
    'A wrapper library to read, manipulate and write data' +
    ''
)
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.doctest',
    'sphinx.ext.intersphinx',
    'sphinx.ext.viewcode',
]
intersphinx_mapping = {
    'pyexcel': ('http://pyexcel.readthedocs.io/en/latest/', None),
}
templates_path = ['_templates']
source_suffix = '.rst'
master_doc = 'index'

project = u'pyexcel-yuri'
copyright = u'Yuri'
version = '0.0.1'
release = '0.0.1'
exclude_patterns = []
pygments_style = 'sphinx'
html_theme = 'default'
html_static_path = ['_static']
htmlhelp_basename = 'pyexcel-xlsxdoc'
latex_elements = {}
latex_documents = [
    ('index', 'pyexcel-xlsx.tex',
     'pyexcel-xlsx Documentation',
     'Onni Software Ltd.', 'manual'),
]
man_pages = [
    ('index', 'pyexcel-xlsx',
     'pyexcel-xlsx Documentation',
     [u'Onni Software Ltd.'], 1)
]
texinfo_documents = [
    ('index', 'pyexcel-xlsx',
     'pyexcel-xlsx Documentation',
     'Onni Software Ltd.', 'pyexcel-xlsx',
     DESCRIPTION,
     'Miscellaneous'),
]
