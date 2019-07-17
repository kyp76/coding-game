import os

# w: width of the building.
# h: height of the building.
 # the direction of the bombs from batman's current location (U, UR, R, DR, D,
 # DL, L or UL, Down, Up, Right, Left)

w = 4
h = 4

class Gird:
    '''
    define Grid
    '''
    def __init__(self, width=4, height=4):
        self.width = width
        self.height = height

    def get(self):
        return self.width, self.height
    def set(self, w, h):
	    self.width = w
	    self.height = h


