"""
Setup module.
"""
from setuptools import setup

from sphinxcadquery import __version__


setup(
    name='sphinxcadquery',
    version=__version__,
    description=
        'An extension to visualize CadQuery 3D parts in your Sphinx documentation',
    long_description="""TODO""",
    url='https://github.com/Peque/sphinxcadquery',
    author='Miguel Sánchez de León Peque',
    author_email='peque@neosit.es',
    license='BSD License',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Topic :: Documentation',
        'Topic :: Software Development',
        'Topic :: Utilities',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Framework :: Sphinx :: Extension',
    ],
    packages=['sphinxcadquery'],
    package_data={
        'sphinxcadquery': [
            'sphinxcadquerystatic/*',
        ],
    },
    install_requires=[
        'sphinx',
    ],
)
