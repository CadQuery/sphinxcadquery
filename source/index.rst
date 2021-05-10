
Example 1
^^^^^^^^^

.. cadquery::
   
   import paramak
   result = paramak.RotateStraightShape(
    points=[
        (400, 100),
        (400, 200),
        (600, 200),
        (600, 100)
           ],
    rotation_angle = 180
   ).solid
