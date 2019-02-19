sphinxcadquery
==============

An extension to visualize CadQuery 3D files in your Sphinx documentation.

.. code::

   pip install sphinxcadquery


Usage
-----

Enable the Sphinx extension(s) in your ``conf.py`` file:

.. code:: python

   extensions = [
       '...',
       'sphinxcadquery.sphinxcadquery',
   ]

Then you can use the ``.. cadquery::`` directive in your documentation:

.. code:: sphinx

   .. cadquery:: ../3d/mydesign.py
      :select: mypart

In ``mypart`` you must provide the name of the object (part) you want to
visualize. If none is provided, the default is to try to load a part named
``part``.

You may want to play with the supported options for a customized look:

.. code:: sphinx

   .. cadquery:: ../3d/mydesign.py
      :select: mypart
      :rotation: true
      :color: #ff00ff
      :background: #222222
      :width: 80%
      :height: 200px
      :gridsize: 20.
      :griddivisions: 20


Notes
-----

Thingiview files are taken from `https://github.com/iXce/thingiview.js`__,
a fork of `https://github.com/tbuser/thingiview.js`__.  See the original
project for their respective license (LGPL).
