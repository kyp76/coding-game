import pytest
from program import Batman


def test_batman_is_instance():
    bat = Batman()
    assert isinstance(bat, Batman)


def test_bat_taken_5_argument():
    bat = Batman(width=6, height=5, bat_x=4, bat_y=3)
    assert bat.width == 6
    assert bat.height == 5
    assert bat.bat_x == 4
    assert bat.bat_y == 3
    assert bat.dir == ""


def test_grid_has_getter_and_return_tuple():
    bat = Batman(width=4, height=5)
    correct_values = [(0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (1, 0), (1, 1),
                      (1, 2), (1, 3), (1, 4), (2, 0), (2, 1), (2, 2), (2, 3),
                      (2, 4), (3, 0), (3, 1), (3, 2), (3, 3), (3, 4)]
    assert bat.get() ==  correct_values

def test_bat_has_setter_and_modify_value():
    bat = Batman(4, 6)
    new_gird = [(0, 0), (1, 1)]
    new_direction = "L"
    bat.set(new_direction=new_direction)
    #assert bat.white_grid == new_gird
    assert bat.dir == "L"


def test_bat_return_expected_white_bat_if_direction_is_up():
    bat = Batman(width=4, height=4, bat_x=3, bat_y=2)
    bat.set("U")
    white_gird = bat.get()
    assert set(white_gird) == set([
        (0, 1),(0, 0), (3, 0),(3, 1),(2, 1), (2, 0),(1, 0), (1, 1)
    ])


def test_bat_return_expected_white_bat_if_direction_is_down():
    bat = Batman(width=4, height=4, bat_x=3, bat_y=2)
    bat.set('D')
    white_gird = bat.get()
    assert set(white_gird) == set([
        (1, 2),(3, 2),(1, 3),(3, 3), (2, 3),(2, 2),(0, 3),(0, 2)
    ])


def test_grid_return_expected_white_bat_if_direction_is_left():
    bat = Batman(width=4, height=4, bat_x=3, bat_y=2)
    bat.set('L')
    white_gird = bat.get()
    assert set(white_gird) == set([
        (0, 0),
        (0, 1),
        (0, 2),
        (0, 3),
        (1, 0),
        (1, 1),
        (1, 2),
        (1, 3),
        (2, 0),
        (2, 1),
        (2, 2),
        (2, 3)
    ])


def test_grid_return_expected_white_bat_if_direction_is_right():
    bat = Batman(width=4, height=4, bat_x=3, bat_y=2)
    bat.set('R')
    white_gird = bat.get()
    assert set(white_gird) == set([(3, 0), (3, 1), (3, 2), (3, 3)])



def test_grid_return_expected_white_bat_if_direction_is_up_and_right():
    bat = Batman(width=4, height=4, bat_x=3, bat_y=2)
    bat.set('UR')
    white_gird = bat.get()
    correct_values = [(3, 0), (3, 1)]
    assert correct_values == white_gird


def test_if_jump_return_is_present_on_white_bat():
    bat = Batman(width=4, height=4, bat_x=3, bat_y=2)
    white_gird = bat.get()
    value = bat.jump()
    assert value in white_gird


def test_bat_create_a_simple_map():
    width = 4
    height = 4
    map = Batman.create_map(start_x=0, end_x=width, start_y=0, end_y=height)
    expected_map = [
        (0, 0),
        (0, 1),
        (0, 2),
        (0, 3),
        (1, 0),
        (1, 1),
        (1, 2),
        (1, 3),
        (2, 0),
        (2, 1),
        (2, 2),
        (2, 3),
        (3, 0),
        (3, 1),
        (3, 2),
        (3, 3),
    ]
    assert expected_map == map


def test_bat_is_set_and_batman_jump_to_a_new_bat():
   bat = Batman(width=4, height=4, bat_x=3, bat_y=2)
   bat.set("UR")
   print(bat.map)
   for el in range(2):
       print("el is : {}".format(el))
       value = bat.jump()
       print('value is {}'.format(value))
       bat.set(new_direction= "R")
       jump = bat.jump()
       print(jump)
       assert  bat.get() == []



