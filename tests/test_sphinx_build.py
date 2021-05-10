
import subprocess


class TestSphinxBuild():

    def test_building_example_docs(self):
        """Builds documentation that contains a few example use cases"""

        subprocess.check_output(['sphinx-build', '-b', 'html', './tests/example', './build/html/'])
