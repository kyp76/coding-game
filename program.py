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

    def __init__(self, width=4, height=4, bat_x=2, bat_y=2):
        self.width = width
    def __init__(self, width=4, height=4, bat_x=2, bat_y=2):
        self.width = width
        self.height = height
        self.dir = ""
        self.bat_x = bat_x
        self.bat_y = bat_y
        self.map = []
        print(f'X bat is {self.bat_x}')
        print(f'Y bat is {self.bat_y}')
        self.generate_map()

    def get(self):
        return list((self.map))

    def set(self, new_direction):
        self.dir = new_direction
        tmp = {0: set(self.map)}
        self.generate_map()
        tmp[1] = set(self.map)

        print(f'tmp dict in set {tmp}')
        self.map = list(tmp[0].intersection(tmp[1]))
        print(self.map)


    def generate_map(self):
        if len(self.dir) == 1 or len(self.dir) == 0:
            self.engine(self.dir)
        else:
            tmp = {}
            for index, el in enumerate(self.dir):
                self.engine(el)
                tmp[index] = set(self.map)
            self.map = tmp[0].intersection(tmp[1])

    @staticmethod
    def create_map(start_x, end_x, start_y, end_y):
        map = []
        for a in range(start_x, end_x):
            for b in range(start_y, end_y):
                map.append((a, b))
        return map

    def engine(self, engine_dir):
        if engine_dir =='':
            self.map = self.create_map(0, self.width , 0 , self.height )
        elif engine_dir == "U":
            #print("it is U")
            self.map = self.create_map(0, self.width , 0, self.bat_y)
        elif engine_dir == "D":
            #print("it is D")
            self.map = self.create_map(0, self.width , self.bat_y, self.height)
        elif engine_dir == "L":
            #print("it is L")
            self.map = self.create_map(0, self.bat_x , 0, self.height)
        elif engine_dir == "R":
            #print("it is R")
            self.map = self.create_map(
                self.bat_x , self.width+ 1, 0 , self.height +1
            )

    def jump(self):
        index = (len(self.map) // 2) - 1
        jump = list(self.map)[index]
        return jump
