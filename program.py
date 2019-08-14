import os

# w: width of the building.
# h: height of the building.
# the direction of the bombs from batman's current location (U, UR, R, DR, D,
# DL, L or UL, Down, Up, Right, Left)

w = 4
h = 4


class Batman:
    """
    define Batman
    """

    def __init__(self, width=4, height=4, direction="U", bat_x=2, bat_y=2):
        self.width = width
        self.height = height
        self.dir = direction
        self.bat_x = bat_x
        self.bat_y = bat_y
        self.white_grid = []
        self.generate_white_gird()

    def get(self):
        return list((self.white_grid))

    def set(self, new_direction, new_gird, new_bat_x, new_bat_y):
        self.dir = new_direction
        print("print white_gird is Bat {} before".format(self.white_grid))
        self.white_grid = new_gird
        print("print white_gird is Bat {} after ".format(self.white_grid))
        self.bat_x = new_bat_x
        self.bat_y = new_bat_y

    def generate_white_gird(self):
        if len(self.dir) == 1:
            self.engine(self.dir, self.white_grid)
            return self.white_grid
        else:
            tmp = {}
            for index, el in enumerate(self.dir):
                tmp_list= []
                tmp[index] = set(self.engine(el,tmp_list))
            self.white_grid = tmp[0].intersection(tmp[1])
            return self.white_grid

    def create_map(self, start_x, end_x, start_y, end_y):
        map = []
        for a in range(start_x, end_x):
            for b in range(start_y, end_y):
                map.append((a,b))
        return map

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

    def jump(self):
        index = (len(self.white_grid)//2) - 1
        jump = list(self.white_grid)[index]
        return jump
