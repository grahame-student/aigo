from unittest import TestCase

from aigo.types.direction import Direction
from aigo.types.point import Point
from hamcrest import assert_that, equal_to


class TestPoint(TestCase):
    def test_neighbours_returns_point_above_in_first_element(self):
        point = Point(5, 5)
        assert_that(point.neighbours()[Direction.up], equal_to(Point(4, 5)))

    def test_neighbours_returns_point_below_in_second_element(self):
        point = Point(5, 5)
        assert_that(point.neighbours()[Direction.down], equal_to(Point(6, 5)))

    def test_neighbours_returns_point_to_left_in_third_element(self):
        point = Point(5, 5)
        assert_that(point.neighbours()[Direction.left], equal_to(Point(5, 4)))

    def test_neighbours_returns_point_to_right_in_fourth_element(self):
        point = Point(5, 5)
        assert_that(point.neighbours()[Direction.right], equal_to(Point(5, 6)))
