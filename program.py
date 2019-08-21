import os

# w: width of the building.
# h: height of the building.
# the direction of the bombs from batman's current location (U, UR, R, DR, D,
# DL, L or UL, Down, Up, Right, Left)

# w = 4
# h = 4


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
        # print(f'X bat is {self.bat_x}')
        # print(f'Y bat is {self.bat_y}')
        self.generate_map()
        import pdb

    def get(self):
        return list((self.map))

    def set(self, new_direction):
        self.dir = new_direction
        # print("Debug messages... Direction: ",self.dir,  file=sys.stderr)
        tmp = {}
        tmp = {0: set(self.map)}
        self.generate_map()
        tmp[1] = set(self.map)

        # print("Debug messages...tmp  in set is ",tmp,  file=sys.stderr)
        # print(f'tmp dict in set {tmp}')
        # print("Debug messages...tmp[0]  in set is ",tmp[0],  file=sys.stderr)
        # print("Debug messages...tmp[1]  in set is ",tmp[1],  file=sys.stderr)
        self.map = list(tmp[0].intersection(tmp[1]))
        # print("Debug messages...Map  in set is ",self.map,  file=sys.stderr)
        # print(self.map)

    def generate_map(self):
        #if len(self.dir) == 1 or len(self.dir) == 0:
        #    self.engine(self.dir)
        #else:
        #    tmp = {}
        #    for index, el in enumerate(self.dir):
        #        self.engine(el)
        #        tmp[index] = set(self.map)
        #    # print("Debug messages... tmp in generate map:",tmp,  file=sys.stderr)
        #    self.map = tmp[0].intersection(tmp[1])
        #    # print("Debug messages... Map in generate map:",self.map,  file=sys.stderr)
        print("\\\\\\ {}".format(self.dir))
        if len(self.dir) ==2:
            tmp = {}
            print("//// {}".format(self.dir))
            for index, el in enumerate(self.dir):
                print('#### {}'.format(el))
                self.engine(el)
                tmp[index] = set(self.map)
            # print("Debug messages... tmp in generate map:",tmp,  file=sys.stderr)
            print("test du tmp {}".format(tmp))
            self.map = tmp[0].intersection(tmp[1])
            # print("Debug messages... Map in generate map:",self.map,  file=sys.stderr)
        else:
            print('je passe pas la ? ')
            self.engine(self.dir)

    @staticmethod
    def create_map(start_x, end_x, start_y, end_y):
        map = []
        for a in range(start_x, end_x):
            for b in range(start_y, end_y):
                map.append((a, b))
        return map

    def engine(self, engine_dir):
        if engine_dir == "":
            self.map = self.create_map(0, self.width, 0, self.height)
        elif engine_dir == "U":
            # print("it is U")
            self.map = self.create_map(0, self.width, 0, self.bat_y + 1)
        elif engine_dir == "D":
            # print("it is D")
            self.map = self.create_map(0, self.width, self.bat_y + 1, self.height)
            print(" map in dir D {}".format(self.map))
            print(" bat_x in dir D {}".format(self.bat_x))
            print(" bat_y in dir D {}".format(self.bat_y))
        elif engine_dir == "L":
            # print("it is L")
            self.map = self.create_map(0, self.bat_x + 1, 0, self.height)
        elif engine_dir == "R":
            # print("it is R")
            self.map = self.create_map(self.bat_x + 1, self.width, 0, self.height)

    def jump(self):
        if len(self.map) == 1:
            return self.map[0]
        else:
            index = (len(self.map) // 2) - 1
            jump = list(self.map)[index]
            self.bat_x = jump[0]
            self.bat_y = jump[1]
            self.map.pop(index)
            print(self.map)
            return jump
