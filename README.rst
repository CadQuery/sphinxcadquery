sphinxcadquery
==============

An extension to visualize CadQuery 3D files in your Sphinx documentation.

.. code::

   pip install sphinxcadquery

Of course, ``cadquery`` needs to be installed as well.


Usage
-----

Enable the Sphinx extension in your ``conf.py`` file:

.. code:: python

   extensions = [
       '...',
       'sphinxcadquery.sphinxcadquery',
   ]

Then you can use the ``.. cadquery::`` directive in your documentation:

.. code:: rest

   .. cadquery::

      result = cadquery.Workplane("XY").box(2, 2, 2)

You may provide a source code file instead:

.. code:: rest

   .. cadquery:: ../3d/mydesign.py


Options
-------

By default it will try to load a part named ``result`` or ``part`` in that
source code. You may change that by providing an explicit name to select:

.. code:: rest

   .. cadquery:: ../3d/mydesign.py
      :select: mypart

You may want to play with the supported options for a customized look:

.. code:: rest

   .. cadquery::
      :select: mypart
      :include-source: true
      :color: #ff00ff
      :width: 80%
      :height: 200px
      :gridsize: 20.
      :griddivisions: 20

      mypart = cadquery.Workplane("XY").box(2, 2, 2)


Global options
--------------

You may as well configure some options globally, by setting the corresponding
variable in your ``conf.py`` file:

.. code:: python

   # Define a different default color
   sphinxcadquery_color = '#bb0000'
   # By default, always show the source code above the scene
   sphinxcadquery_include_source = True
