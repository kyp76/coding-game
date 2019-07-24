import os

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
        self.tmp_gird = []

    def get(self):
        return self.width, self.height, self.bat_x, self.bat_y

    def set(self, bat_x, bat_y, new_gird, new_direction):
        self.bat_x = bat_x
        self.bat_y = bat_y
        self.white_grid = new_gird
        self.dir = new_direction

    def generate_white_gird(self):
        if len(self.dir) == 1:
            self.engine(self.dir, self.white_grid)
            return self.white_grid
        else:
            tmp = {}
            for index, el in enumerate(self.dir):
                tmp_list= []
                print(el)
                print(index)
                tmp[index] = set(self.engine(el,tmp_list))
            self.white_grid = tmp[0].intersection(tmp[1])
            print(self.white_grid)
            return list(self.white_grid)

    def engine(self, engine_dir, engine_list):
        if engine_dir == "U":
            for a in range(self.width):
                for b in range(self.bat_y, self.height):
                    engine_list.append((a, b))

        elif engine_dir == "D":
            for a in range(self.width):
                for b in range(0, self.bat_y):
                    engine_list.append((a, b))
        elif engine_dir == "L":
            for a in range(0, self.bat_x - 1):
                for b in range(self.height):
                    engine_list.append((a, b))
        elif engine_dir == "R":
            for a in range(self.bat_x - 1, self.width):
                for b in range(self.height):
                    engine_list.append((a, b))

        return engine_list


class Batman:
    inital_gird = []

    def __init__(self, correct_gird=[]):
        self.correct_gird = correct_gird
        self.jump_place = list(set(self.correct_gird) - set(self.inital_gird))
        self.random_nb = len(self.jump_place)//2

    def jump(self):
        self.jump = self.jump_place[self.random_nb]
        return self.jump
