import pytest
from program import Gird, Batman


def test_grid_is_instance():
    grid = Gird()
    assert isinstance(grid, Gird)


def test_batman_is_instance():
    bat = Batman()
    assert isinstance(bat, Batman)


def test_gird_taken_5_argument():
    gird = Gird(width=4, height=4, bat_x=4, bat_y=3, direction="R")
    assert gird.width == 4
    assert gird.height == 4
    assert gird.bat_x == 4
    assert gird.bat_y == 3
    assert gird.dir == "R"


def test_grid_has_getter_and_return_tuple():
    gird = Gird(4, 5)
    assert gird.get() == (4, 5, 2, 2)


def test_gird_has_setter_and_modify_value():
    gird = Gird(4, 6)
    new_gird = [(0,0),(1,1)]
    new_direction = 'L'
    gird.set(3, 5, new_gird, new_direction)
    assert gird.bat_x == 3
    assert gird.bat_y == 5
    assert gird.white_grid == new_gird
    assert gird.dir == 'L'

def test_grid_return_expected_white_gird_if_direction_is_up():
    gird = Gird(width=4, height=4, bat_x=3, bat_y=2, direction="U")
    white_gird = gird.generate_white_gird()
    assert white_gird == [
        (0, 2),
        (0, 3),
        (1, 2),
        (1, 3),
        (2, 2),
        (2, 3),
        (3, 2),
        (3, 3),
    ]


def test_grid_return_expected_white_gird_if_direction_is_down():
    gird = Gird(width=4, height=4, bat_x=3, bat_y=2, direction="D")
    white_gird = gird.generate_white_gird()
    assert white_gird == [
        (0, 0),
        (0, 1),
        (1, 0),
        (1, 1),
        (2, 0),
        (2, 1),
        (3, 0),
        (3, 1),
    ]


def test_grid_return_expected_white_gird_if_direction_is_left():
    gird = Gird(width=4, height=4, bat_x=3, bat_y=2, direction="L")
    white_gird = gird.generate_white_gird()
    assert white_gird == [
        (0, 0),
        (0, 1),
        (0, 2),
        (0, 3),
        (1, 0),
        (1, 1),
        (1, 2),
        (1, 3),
    ]


def test_grid_return_expected_white_gird_if_direction_is_right():
    gird = Gird(width=4, height=4, bat_x=3, bat_y=2, direction="R")
    white_gird = gird.generate_white_gird()
    assert white_gird == [
        (2, 0),
        (2, 1),
        (2, 2),
        (2, 3),
        (3, 0),
        (3, 1),
        (3, 2),
        (3, 3),
    ]


def test_batman_take_a_gird():
    gird = Gird(width=4, height=4, bat_x=3, bat_y=2, direction="R")
    white_gird = gird.generate_white_gird()
    print(white_gird)
    bat = Batman(white_gird)
    assert bat.correct_gird == [
        (2, 0),
        (2, 1),
        (2, 2),
        (2, 3),
        (3, 0),
        (3, 1),
        (3, 2),
        (3, 3),
    ]



def test_grid_return_expected_white_gird_if_direction_is_up_and_right():
    gird = Gird(width=4, height=4, bat_x=3, bat_y=2, direction="UR")
    white_gird = gird.generate_white_gird()
    correct_values = [
        (2, 2),
        (2, 3),
        (3, 2),
        (3, 3),
    ]
    #for el in correct_values:
    bat= Batman(white_gird)
    bat.random_nb = 1
    value = bat.jump()
    assert (2,3) ==  value

def test_if_jump_return_is_present_on_white_gird():
    gird = Gird(width=4, height=4, bat_x=3, bat_y=2, direction="R")
    white_gird = gird.generate_white_gird()
    bat = Batman(white_gird)
    value = bat.jump()
    assert value in bat.jump_place

def test_if_jump_return_is_expected_value_on_white_gird():
    gird = Gird(width=4, height=4, bat_x=3, bat_y=2, direction="R")
    white_gird = gird.generate_white_gird()
    bat = Batman(white_gird)
    bat.random_nb = 2
    value = bat.jump()
    assert (3, 0) == bat.jump_place[2]



