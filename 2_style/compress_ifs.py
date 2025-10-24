# STYLE ***************************************************************************
# content = assignment (Python Advanced)
#
# modified by = Elena Giuliani
#
# date    = 2025-10-20
# email   = contact@alexanderrichtertd.com
#**********************************************************************************

# SOLUTION 1
# with loop
def set_color_v1(ctrlList=None, color_input=None):
    override_color = [4, 13, 25, 17, 17, 15, 6, 16]

    for ctrlName in ctrlList:
        try:
            mc.setAttr(ctrlName + 'Shape.overrideEnabled', 1)
        except:
            pass

        try:
            for number in range(1,9):
                if number == color_input:
                    print(f'TEST v1: {ctrlName}, number {number}, color input {color_input}, override color {override_color[int(color_input - 1)]}')
                    #mc.setAttr(ctrlName + 'Shape.overrideColor', {override_color[int(color_input - 1)]}')
        except:
            pass

set_color_v1(['circle', 'circle1'], 8)

#-----------------------------------------------------------
# SOLUTION 2
# with looping through dictionary
def set_color_v2(ctrlList=None, color=None):
    override_color = [4, 13, 25, 17, 17, 15, 6, 16]
    color_dict = dict(zip(range(1,9), override_color))

    for ctrlName in ctrlList:
        try:
            mc.setAttr(ctrlName + 'Shape.overrideEnabled', 1)
        except:
            pass

        try:
            for key in color_dict:
                if color == key:
                    print(f'TEST v2: {ctrlName}, override color {color_dict[key]}')
                    #mc.setAttr(ctrlName + 'Shape.overrideColor', {color_dict[key]}')
        except:
            pass

set_color_v2(['circle', 'circle1'], 7)




# BRIEF
# COMMENT --------------------------------------------------
# Not optimal
def set_color(ctrlList=None, color=None):

    for ctrlName in ctrlList:
        try:
            mc.setAttr(ctrlName + 'Shape.overrideEnabled', 1)
        except:
            pass

        try:
            if color == 1:
                mc.setAttr(ctrlName + 'Shape.overrideColor', 4)

            elif color == 2:
                mc.setAttr(ctrlName + 'Shape.overrideColor', 13)

            elif color == 3:
                mc.setAttr(ctrlName + 'Shape.overrideColor', 25)

            elif color == 4:
                mc.setAttr(ctrlName + 'Shape.overrideColor', 17)

            elif color == 5:
                mc.setAttr(ctrlName + 'Shape.overrideColor', 17)

            elif color == 6:
                mc.setAttr(ctrlName + 'Shape.overrideColor', 15)

            elif color == 7:
                mc.setAttr(ctrlName + 'Shape.overrideColor', 6)

            elif color == 8:
                mc.setAttr(ctrlName + 'Shape.overrideColor', 16)
        except:
            pass

# EXAMPLE
# set_color(['circle','circle1'], 8)
