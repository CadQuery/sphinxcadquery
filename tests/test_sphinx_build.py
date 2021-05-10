
import unittest
import subprocess


class TestSphinxBuild(unittest.TestCase):

    def test_building_example_docs(self):
        """Builds documentation that contains a few example use cases"""

        subprocess.check_output(['sphinx-build', '-b', 'html', './source', './build/html/'])
