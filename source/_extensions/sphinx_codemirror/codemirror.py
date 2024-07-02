import os
import uuid
from docutils import nodes
from docutils.parsers.rst import Directive, directives
from sphinx.util.fileutil import copy_asset

class CodeMirrorNode(nodes.General, nodes.Element):
    pass

class CodeMirrorDirective(Directive):
    has_content = True
    option_spec = {
        'class' : directives.class_option,
    }

    def run(self):
        
        self.assert_has_content()
        content = '\n'.join(self.content)
        code_id = str(uuid.uuid4())

        custom_class = ' '.join(self.options.get('class', []))
        container_class = f'codemirror-container {custom_class}'

        html = f'''
        <div class="{container_class}" id="editor-{code_id}">
            <textarea style="display:none;">{content}</textarea>
        </div>
        '''
        return [nodes.raw('', html, format='html')]

def add_codemirror_assets(app):
    static_path = os.path.join(os.path.dirname(__file__), '_static')
    for asset in ['css/codemirror.min.css','mode/python/python.min.js', 'js/codemirror.min.js','js/sphinx_codemirror.js']:
        copy_asset(os.path.join(static_path, asset), os.path.join(app.outdir, '_static/sphinx_codemirror'))

    app.add_css_file('sphinx_codemirror/codemirror.min.css')
    app.add_js_file('sphinx_codemirror/codemirror.min.js')
    app.add_js_file('sphinx_codemirror/python.min.js')
    app.add_js_file('sphinx_codemirror/sphinx_codemirror.js')

def setup(app):
    
    app.add_directive('codemirror', CodeMirrorDirective)
    app.connect('builder-inited', add_codemirror_assets)
    
    return {
        'version': '0.1',
        'parallel_read_safe': True,
        'parallel_write_safe': True,
    }
