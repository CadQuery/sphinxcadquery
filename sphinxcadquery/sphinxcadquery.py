import os
from hashlib import sha256
import importlib
import json
import logging
import textwrap
from uuid import uuid4
from pathlib import Path
from pkg_resources import resource_filename
from tempfile import NamedTemporaryFile

from docutils import nodes
from docutils.parsers.rst import Directive
from docutils.parsers.rst import directives

from sphinx.transforms import SphinxTransform
from sphinx.util.docutils import LoggingReporter
from sphinx.util.fileutil import copy_asset

import cadquery

from . import __version__


logger = logging.getLogger(__name__)

common_part_names = ['result', 'part']
common_source_header = [
    'import cadquery',
    'import cadquery as cq',
]
raw_html_template = """
<div class="sphinxcadqueryview", style="width:{width};height:{height}">
    <script>
        var parent = document.scripts[ document.scripts.length - 1 ].parentNode;
        parent.fname = "{parturi}";
        parent.color = "{color}";
        parent.gridsize = "{gridsize}";
        parent.griddivisions = "{griddivisions}";
    </script>
</div>
"""


def directive_truefalse(argument):
    return directives.choice(argument, ('true', 'false'))


def get_handler(fname):
    loader = importlib.machinery.SourceFileLoader('source', str(fname))
    return loader.load_module('source')


def find_part(module, name):
    """
    Try to find the 3D part to visualize.

    If no part name is provided, it will try with a list of default/usual
    candidates.
    """
    source = module.__dict__
    if name:
        candidates = [name]
    else:
        candidates = common_part_names
    for candidate in candidates:
        if candidate in source.keys():
            return source[candidate]
    raise KeyError('Could not find `%s` to visualize!' % candidates[0])


class CadQueryDirective(Directive):
    has_content = True
    required_arguments = 0
    optional_arguments = 1
    final_argument_whitespace = True
    option_spec = {
        'select': directives.unchanged,
        'include-source': bool,
        'color': directives.unchanged,
        'background': directives.unchanged,
        'rotation': directive_truefalse,
        'width': directives.unchanged,
        'height': directives.unchanged,
        'gridsize': float,
        'griddivisions': int,
    }

    def run(self):

        doc_source_name = self.state.document.attributes['source']

        self.options.setdefault('include-source',
                                setup.app.config.sphinxcadquery_include_source)
        self.options.setdefault('color', setup.app.config.sphinxcadquery_color)

        if len(self.arguments):
            fname = Path(setup.app.srcdir) / self.arguments[0]
            fname = fname.resolve()
            handle = get_handler(fname)
        else:
            with NamedTemporaryFile() as named:
                fname = named.name
                with open(fname, 'w') as tmp:
                    tmp.write(
                        '\n'.join(common_source_header + self.content.data))
                handle = get_handler(fname)

        select = self.options.get('select', None)
        part = find_part(handle, select)
        content = cadquery.exporters.toString(part, 'TJS')
        digest = sha256(content.encode('utf')).hexdigest()

        fpath = Path('_static') / 'sphinxcadquery'
        fname = Path(digest).with_suffix('.tjs')
        outputdir = Path(setup.app.builder.outdir) / fpath
        outputdir.mkdir(parents=True, exist_ok=True)
        outputfname = outputdir / fname

        with open(outputfname, 'w') as outputfile:
            outputfile.write(content)

        source_path = Path(doc_source_name)
        depth = \
            len(source_path.parent.relative_to(Path(setup.app.srcdir)).parents)
        relative_uri = Path('.')
        for _ in range(depth):
            relative_uri /= '../'

        raw_html = raw_html_template.format(
            parturi=relative_uri / fpath / fname,
            color=self.options['color'],
            width=self.options.get('width', '100%'),
            height=self.options.get('height', '400px'),
            gridsize=self.options.get('gridsize', 100.),
            griddivisions=self.options.get('griddivisions', 20),
        )

        lines = []
        if self.options['include-source']:
            data = textwrap.indent('\n'.join(self.content.data), '    ')
            lines = ['.. code-block:: python', '', *data.splitlines()]
            lines.extend(['', ''])
        lines.extend(['', ''])
        raw_html = textwrap.indent(raw_html, '    ')
        lines.extend(['.. raw:: html', '', *raw_html.splitlines()])
        lines.extend(['', ''])
        self.state_machine.insert_input(lines, source=doc_source_name)
        return []


def copy_asset_files(app, exc):
    if exc is not None:  # build failed
        return
    source = resource_filename(__name__, 'sphinxcadquerystatic')
    copy_asset(source, os.path.join(app.outdir, '_static/sphinxcadquerystatic'))


def setup(app):
    setup.app = app
    app.connect('build-finished', copy_asset_files)
    app.add_javascript('sphinxcadquerystatic/three.js')
    app.add_javascript('sphinxcadquerystatic/AMFLoader.js')
    app.add_javascript('sphinxcadquerystatic/STLLoader.js')
    app.add_javascript('sphinxcadquerystatic/LegacyJSONLoader.js')
    app.add_javascript('sphinxcadquerystatic/jszip.min.js')
    app.add_javascript('sphinxcadquerystatic/OrbitControls.js')
    app.add_javascript('sphinxcadquerystatic/WebGL.js')
    app.add_javascript('sphinxcadquerystatic/main.js')
    app.add_stylesheet('sphinxcadquerystatic/main.css')
    app.add_directive('cadquery', CadQueryDirective)
    app.add_config_value('sphinxcadquery_color', '#99bbdd', 'env')
    app.add_config_value('sphinxcadquery_include_source', False, 'env')
    return {'version': __version__, 'parallel_read_safe': True}
