import pytest
from program import Batman


def test_batman_is_instance():
    bat = Batman()
    assert isinstance(bat, Batman)


def test_bat_taken_5_argument():
    bat = Batman(width=6, height=5, bat_x=4, bat_y=3, direction="R")
    assert bat.width == 6
    assert bat.height == 5
    assert bat.bat_x == 4
    assert bat.bat_y == 3
    assert bat.dir == "R"


def test_grid_has_getter_and_return_tuple():
    bat = Batman(width=4, height=5)
    assert bat.get() == [
        (0, 2),
        (0, 3),
        (0, 4),
        (1, 2),
        (1, 3),
        (1, 4),
        (2, 2),
        (2, 3),
        (2, 4),
        (3, 2),
        (3, 3),
        (3, 4),
    ]


def test_bat_has_setter_and_modify_value():
    bat = Batman(4, 6)
    new_gird = [(0, 0), (1, 1)]
    new_direction = "L"
    bat.set(new_bat_x=3, new_bat_y=5, new_gird=new_gird, new_direction=new_direction)
    assert bat.bat_x == 3
    assert bat.bat_y == 5
    assert bat.white_grid == new_gird
    assert bat.dir == "L"


def test_bat_return_expected_white_bat_if_direction_is_up():
    bat = Batman(width=4, height=4, bat_x=3, bat_y=2, direction="U")
    white_gird = bat.get()
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


def test_bat_return_expected_white_bat_if_direction_is_down():
    bat = Batman(width=4, height=4, bat_x=3, bat_y=2, direction="D")
    white_gird = bat.get()
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


def test_grid_return_expected_white_bat_if_direction_is_left():
    bat = Batman(width=4, height=4, bat_x=3, bat_y=2, direction="L")
    white_gird = bat.get()
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


def test_grid_return_expected_white_bat_if_direction_is_right():
    bat = Batman(width=4, height=4, bat_x=3, bat_y=2, direction="R")
    white_gird = bat.get()
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
    bat = Batman(width=4, height=4, bat_x=3, bat_y=2, direction="R")
    # white_gird = bat.get()
    white_gird = bat.get()
    bat.set(new_gird=white_gird, new_direction="R", new_bat_x=4, new_bat_y=4)
    assert bat.white_grid == [
        (2, 0),
        (2, 1),
        (2, 2),
        (2, 3),
        (3, 0),
        (3, 1),
        (3, 2),
        (3, 3),
    ]


def test_grid_return_expected_white_bat_if_direction_is_up_and_right():
    bat = Batman(width=4, height=4, bat_x=3, bat_y=2, direction="UR")
    white_gird = bat.get()
    correct_values = [(2, 2), (2, 3), (3, 2), (3, 3)]
    value = bat.jump()
    assert (2, 3) == value


def test_if_jump_return_is_present_on_white_bat():
    bat = Batman(width=4, height=4, bat_x=3, bat_y=2, direction="R")
    white_gird = bat.get()
    # bat.set(new_gird= white_gird, new_direction= "R", new_bat_x = 4,
    #        new_bat_y=4)
    value = bat.jump()
    assert value in white_gird


def test_bat_create_a_simple_map():
    width = 4
    height = 4
    bat = Batman(width=width, height=height, bat_x=3, bat_y=2, direction="R")
    map = bat.create_map(start_x= 0, end_x= width,start_y=0, end_y=height)
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


# def test_bat_is_set_and_batman_jump_to_a_new_bat():
#    bat = Batman(width=4, height=4, bat_x=3, bat_y=2, direction="UR")
#    print(bat.white_grid)
#    for el in range(2):
#        print("el is : {}".format(el))
#        new_gird = bat.get()
#        print('new_grid is {}'.format(new_gird))
#        value = bat.jump()
#        print('value is {}'.format(value))
#        bat.set(new_gird= new_gird, new_direction= "R", new_bat_x = 2,
#                new_bat_y=3)
#        bat.generate_white_gird()
#    assert 0
#
