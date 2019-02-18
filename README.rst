sphinxstl
=========

An extension to visualize STL files in your Sphinx documentation.

.. code::

   pip install sphinxstl


Usage
-----

Enable the Sphinx extension(s) in your ``conf.py`` file:

.. code:: python

   extensions = [
       '...',
       'sphinxstl.sphinxstl',
   ]

Then you can use the ``.. stl::`` directive in your documentation:

.. code:: sphinx

   .. stl:: http://upload.wikimedia.org/wikipedia/commons/9/93/Utah_teapot_%28solid%29.stl

You may want to play with the supported options for a customized look:

.. code:: sphinx

   .. stl:: http://upload.wikimedia.org/wikipedia/commons/9/93/Utah_teapot_%28solid%29.stl
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
