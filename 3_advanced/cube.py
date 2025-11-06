# ADVANCED ***************************************************************************
# content = assignment
#
# modified by = Elena Giuliani
#
# date    = 2025-10-28
# email   = contact@alexanderrichtertd.com
#************************************************************************************

"""
CUBE CLASS

1. CREATE an abstract class "Cube" with the functions:
   translate(x, y, z), rotate(x, y, z), scale(x, y, z) and color(R, G, B)
   All functions store and print out the data in the cube (translate, rotate, scale and color).

2. ADD an __init__(name) and create 3 cube objects.

3. ADD the function print_status() which prints all the variables nicely formatted.

4. ADD the function update_transform(ttype, value).
   "ttype" can be "translate", "rotate" and "scale" while "value" is a list of 3 floats.
   This function should trigger either the translate, rotate or scale function.

   BONUS: Can you do it without using ifs?

5. CREATE a parent class "Object" which has a name, translate, rotate and scale.
   Use Object as the parent for your Cube class.
   Update the Cube class to not repeat the content of Object.

"""

class Object:
    def __init__(self, name):
        self.name = name
        
        # default attributes
        self.translate = [0, 0, 0]
        self.rotate = [0, 0, 0]
        self.scale = [1, 1, 1]

#---------------------------------------------
class Cube(Object):
    def __init__(self, name):
        super(Cube, self).__init__(name)

        # default attributes
        self.color = [1, 1, 1]

    def translate(self, x, y, z):
        self.translate = [x, y, z]
        print(self.translate)

    def rotate(self, x, y, z):
        self.rotate = [x, y, z]
        print(self.rotate)
    
    def scale(self, x, y, z):
        self.scale = [x, y, z]
        print(self.scale)
    
    def color(self, R, G, B):
        self.color = [R, G, B]
        print(self.color)

    def print_status(self):
        print(f'\nProp      : {self.name}\nTranslate : {self.translate} \nRotate    : {self.rotate} \nScale     : {self.scale} \nColor     : {self.color}\n')

    def update_transform(self, ttype, value):
        gizmo = {'translate' :  self.translate,
                 'rotate'    :  self.rotate,
                 'scale'     :  self.scale
                 }
        
        self.value = [0.0, 0.0, 0.0]

        for key, transform in gizmo.items():
            if key == ttype:
                return transform


table = Cube('table_AA')
table.translate = [2, 5, 8]
table.scale = [0.4, 6.5, 1.0]
table.print_status()
print(table.update_transform('translate', [1.0, 3.5, 8.3]))

chair = Cube('chair_AA')
bed   = Cube('bed_AA')