import os
import json
import logging
from uuid import uuid4
from pkg_resources import resource_filename

from docutils import nodes
from docutils.parsers.rst import Directive
from docutils.parsers.rst import directives

from sphinx.transforms import SphinxTransform
from sphinx.util.docutils import LoggingReporter
from sphinx.util.fileutil import copy_asset

from . import __version__


logger = logging.getLogger(__name__)

raw_html_template = """
   <script>
     window.addEventListener('load', function() {{
       thingiurlbase = "_static/thingiview";
       thingiview = new Thingiview("{thingid}");
       thingiview.setObjectColor('{color}');
       thingiview.setBackgroundColor('{background}');
       thingiview.setRotation({rotation});
       thingiview.initScene();
       thingiview.loadSTL("https://upload.wikimedia.org/wikipedia/commons/b/b1/Sphericon.stl");
     }}, false);
   </script>

   <div id="{thingid}" style="width:{width};height:{height}"></div>
"""


def directive_truefalse(argument):
    return directives.choice(argument, ('true', 'false'))


class STLDirective(Directive):
    has_content = True
    option_spec = {
        'color': directives.unchanged,
        'background': directives.unchanged,
        'rotation': directive_truefalse,
        'width': directives.unchanged,
        'height': directives.unchanged,
    }

    def run(self):
        raw_html = raw_html_template.format(
            color=self.options.get('color', '#99ccff'),
            background=self.options.get('background', '#ffffff'),
            rotation=self.options.get('rotation', 'true'),
            width=self.options.get('width', '100%'),
            height=self.options.get('height', '400px'),
            thingid=uuid4().hex,
        )
        stl = nodes.raw('', raw_html, format='html')
        return [stl]


def copy_asset_files(app, exc):
    asset_files = [
        resource_filename(__name__, 'thingiview'),
    ]
    if exc is None:  # build succeeded
        for path in asset_files:
            copy_asset(path, os.path.join(app.outdir, '_static/thingiview'))


def setup(app):
    app.connect('build-finished', copy_asset_files)
    app.add_javascript('thingiview/three.min.js')
    app.add_javascript('thingiview/plane.js')
    app.add_javascript('thingiview/thingiview.js')
    app.add_directive('stl', STLDirective)
    return {'version': __version__, 'parallel_read_safe': True}
