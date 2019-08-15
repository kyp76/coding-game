import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

# w: width of the building.
# h: height of the building.
w, h = [int(i) for i in input().split()]
n = int(input())  # maximum number of turns before game over.
x0, y0 = [int(i) for i in input().split()]



w = 4
h = 4


class Batman:
    """
    define Batman
    """

    def __init__(self, width=4, height=4, bat_x=2, bat_y=2):
        self.width = width
        self.height = height
        #self.dir = direction
        self.bat_x = bat_x
        self.bat_y = bat_y
        self.white_grid = []
        #print(f'X bat is {self.bat_x}')
        #print(f'Y bat is {self.bat_y}')
        #self.generate_white_gird()

    def get(self):
        return list((self.white_grid))

    def set(self, new_direction, new_bat_x, new_bat_y):
        self.dir = new_direction
        #self.white_grid = new_gird
        self.bat_x = new_bat_x
        self.bat_y = new_bat_y
        tmp = {0: set(self.white_grid)}
        self.generate_white_gird()
        print("White-gird posistion 1",self.white_grid, file=sys.stderr)

        tmp[1] = set(self.white_grid)
        print("White-gird posistion 2",self.white_grid, file=sys.stderr)
        #print(f'tmp dict in set {tmp}')
        if tmp[0] == set():
            self.white_gird = tmp[1]
        else:
            self.white_grid = list(tmp[0].intersection(tmp[1]))
        #print(self.white_grid)
        print("White-gird posistion 3",self.white_grid, file=sys.stderr)
        print("Tmp ",tmp, file=sys.stderr)


    def generate_white_gird(self):
        if len(self.dir) == 1:
            self.engine(self.dir)
        else:
            tmp = {}
            for index, el in enumerate(self.dir):
                self.engine(el)
                tmp[index] = set(self.white_grid)
            self.white_grid = tmp[0].intersection(tmp[1])

    #@staticmethod
    def create_map(self, start_x, end_x, start_y, end_y):
        map = []
        for a in range(start_x, end_x):
            for b in range(start_y, end_y):
                map.append((a, b))
        return map

    def engine(self, engine_dir):
        if engine_dir == "U":
            #print("it is U")
            self.white_grid = self.create_map(0, self.width, self.bat_y, self.height)
        elif engine_dir == "D":
            #print("it is D")
            self.white_grid = self.create_map(0, self.width, 0, self.bat_y)
        elif engine_dir == "L":
            #print("it is L")
            self.white_grid = self.create_map(0, self.bat_x , 0, self.height)
        elif engine_dir == "R":

            self.white_grid = self.create_map(
                self.bat_x , self.width, 0 , self.height
            )
            #print(self.white_grid)

    def jump(self):
        index = (len(self.white_grid) // 2) - 1
        jump = list(self.white_grid)[index]
        return jump


# w: width of the building.
# h: height of the building.
# the direction of the bombs from batman's current location (U, UR, R, DR, D,
# DL, L or UL, Down, Up, Right, Left)

# game loop
bat = Batman(width=w, height=h, bat_x=x0, bat_y=y0)
while True:
    bomb_dir = input()  # the direction of the bombs from batman's current location (U, UR, R, DR, D, DL, L or UL)
    print(bomb_dir, file=sys.stderr)
    print("Wigth and Heigth of the building", w, h, file=sys.stderr)
    print(n, file=sys.stderr)
    print("Batman posistion",x0, y0, file=sys.stderr)
    # Write an action using print
    # To debug: print("Debug messages...", file=sys.stderr)

    # value = bat.jump()

    bat.set(new_direction= bomb_dir, new_bat_x = x0, new_bat_y=y0)
    new_gird = bat.get()
    print("print new_gird posistion",new_gird, file=sys.stderr)
    value = bat.jump()
    # the location of the next window Batman should jump to.
    #print(f'{value[0] value[1]}')
    print("{} {}".format(value[0], value[1]))
