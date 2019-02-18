"""
Setup module.
"""
from setuptools import setup

from sphinxstl import __version__


setup(
    name='sphinxstl',
    version=__version__,
    description=
        'An extension to visualize STL files in your Sphinx documentation',
    long_description="""TODO""",
    url='https://github.com/Peque/sphinxstl',
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
    packages=['sphinxstl'],
    package_data={
        'sphinxstl': [
            'thingview',
        ],
    },
    install_requires=[
        'sphinx',
    ],
)
