import os
import random

# w: width of the building.
# h: height of the building.
# the direction of the bombs from batman's current location (U, UR, R, DR, D,
# DL, L or UL, Down, Up, Right, Left)

w = 4
h = 4


class Gird:
    """
    define Grid
    """

    def __init__(self, width=4, height=4, direction="U", bat_x=2, bat_y=2):
        self.width = width
        self.height = height
        self.dir = direction
        self.bat_x = bat_x
        self.bat_y = bat_y
        self.white_grid = []

    def get(self):
        return self.width, self.height, self.bat_x, self.bat_y

    def set(self, bat_x, bat_y):
        self.bat_x = bat_x
        self.bat_y = bat_y

    def generate_white_gird(self):
        if self.dir == "U":
            for a in range(self.width):
                for b in range(self.bat_y, self.height):
                    self.white_grid.append((a, b))
            return self.white_grid

        elif self.dir == "D":
            for a in range(self.width):
                for b in range(0, self.bat_y):
                    self.white_grid.append((a, b))
            return self.white_grid
        elif self.dir == "L":
            for a in range(0, self.bat_x - 1):
                for b in range(self.height):
                    self.white_grid.append((a, b))
            return self.white_grid
        elif self.dir == "R":
            for a in range(self.bat_x - 1, self.width):
                for b in range(self.height):
                    self.white_grid.append((a, b))
            return self.white_grid
        else:
            return self.white_grid


class Batman:
    inital_gird = []

    def __init__(self, correct_gird=[]):
        self.correct_gird = correct_gird
        self.jump_place = list(set(self.correct_gird) - set(self.inital_gird))
        self.random_nb = random.randint(0, len(self.jump_place))

    def jump(self):
        self.jump = self.jump_place[self.random_nb]
        return self.jump
