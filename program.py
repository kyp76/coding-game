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
        print(f'X bat is {self.bat_x}')
        print(f'Y bat is {self.bat_y}')
        self.generate_white_gird()

    def get(self):
        return list((self.white_grid))

    def set(self, new_direction):
        self.dir = new_direction
        #self.white_grid = new_gird
        #self.bat_x = new_bat_x
        #self.bat_y = new_bat_y
        tmp = {0: set(self.white_grid)}
        self.generate_white_gird()
        tmp[1] = set(self.white_grid)

        print(f'tmp dict in set {tmp}')
        self.white_grid = list(tmp[0].intersection(tmp[1]))
        print(self.white_grid)


    def generate_white_gird(self):
        if len(self.dir) == 1:
            self.engine(self.dir)
        else:
            tmp = {}
            for index, el in enumerate(self.dir):
                self.engine(el)
                tmp[index] = set(self.white_grid)
            self.white_grid = tmp[0].intersection(tmp[1])

    @staticmethod
    def create_map(start_x, end_x, start_y, end_y):
        map = []
        for a in range(start_x, end_x):
            for b in range(start_y, end_y):
                map.append((a, b))
        return map

    def engine(self, engine_dir):
        if engine_dir == "U":
            print("it is U")
            self.white_grid = self.create_map(0, self.width, self.bat_y, self.height)
        elif engine_dir == "D":
            print("it is D")
            self.white_grid = self.create_map(0, self.width, 0, self.bat_y)
        elif engine_dir == "L":
            print("it is L")
            self.white_grid = self.create_map(0, self.bat_x , 0, self.height)
        elif engine_dir == "R":
            print("it is R")
            print(self.bat_x)
            print(self.bat_y)
            print(self.height)
            print(self.width)
            print(self.white_grid)
            self.white_grid = self.create_map(
                self.bat_x , self.width, 0 , self.height
            )
            print(self.white_grid)

    def jump(self):
        index = (len(self.white_grid) // 2) - 1
        jump = list(self.white_grid)[index]
        return jump
