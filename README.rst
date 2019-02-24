sphinxcadquery
==============

An extension to visualize CadQuery 3D files in your Sphinx documentation.

.. code::

   pip install sphinxcadquery


Usage
-----

Enable the Sphinx extension in your ``conf.py`` file:

.. code:: python

   extensions = [
       '...',
       'sphinxcadquery.sphinxcadquery',
   ]

Then you can use the ``.. cadquery::`` directive in your documentation:

.. cadquery::

   result = cadquery.Workplane("XY").box(2, 2, 2) \
      .edges("|Z and <Y").chamfer(0.2)

You may provide a source code file instead:

.. code:: sphinx

   .. cadquery:: ../3d/mydesign.py

By default it will try to load a part named ``result`` or ``part`` in that
source code. You may change that by providing a explicit name to select:

.. code:: sphinx

   .. cadquery:: ../3d/mydesign.py
      :select: mypart

You may want to play with the supported options for a customized look:

.. code:: sphinx

   .. cadquery:: ../3d/mydesign.py
      :select: mypart
      :color: #ff00ff
      :width: 80%
      :height: 200px
      :gridsize: 20.
      :griddivisions: 20
