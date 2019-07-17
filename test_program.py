import pytest
from program import Gird


def test_grid_is_instance():
    grid = Gird()
    assert isinstance(grid, Gird)


def test_gird_taken_2_argument():
    gird = Gird(width=4, height=4)
    assert gird.width == 4
    assert gird.height == 4


def test_grid_has_getter_and_return_tuple():
    gird = Gird(4, 5)
    assert gird.get() == (4, 5)


def test_gird_has_setter_and_modify_value():
    gird = Gird(4, 6)
    gird.set(3, 5)
    assert gird.width == 3
    assert gird.height == 5

