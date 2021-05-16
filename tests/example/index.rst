
Example 1
^^^^^^^^^

.. cadquery::

   result = cadquery.Workplane("XY").box(2, 2, 2)


Example 2
^^^^^^^^^

.. cadquery::
   :select: mypart
   :include-source: true
   :color: #ff00ff
   :width: 80%
   :height: 200px
   :gridsize: 20.
   :griddivisions: 20

   mypart = cadquery.Workplane("XY").box(2, 2, 2)

Example 3
^^^^^^^^^

.. cadquery::
   :gridsize: 0

   result = cadquery.Workplane("XY").box(2, 2, 2)
