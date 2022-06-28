from unittest import TestCase

from aigo.go_string import GoString
from aigo.types.player import Player
from aigo.types.point import Point
from hamcrest import assert_that, equal_to, instance_of


class TestGoString(TestCase):
    def test_constructor_sets_colour_to_passed_in_colour(self):
        go_string = GoString(Player.white, [], [])
        assert_that(go_string.colour, equal_to(Player.white))

    def test_constructor_set_stones_to_passed_in_points(self):
        stones = [Point(1, 2), Point(5, 5)]
        go_string = GoString(Player.white, stones, [])
        assert_that(go_string.stones, equal_to(set(stones)))

    def test_constructor_set_stones_to_set_of_passed_in_points(self):
        stones = [Point(5, 5), Point(5, 5)]
        go_string = GoString(Player.white, stones, [])
        assert_that(go_string.stones, equal_to({Point(5, 5)}))

    def test_constructor_set_liberties_to_passed_in_points(self):
        liberties = [Point(1, 2), Point(5, 5)]
        go_string = GoString(Player.white, [], liberties)
        assert_that(go_string.liberties, equal_to(set(liberties)))

    def test_constructor_set_liberties_to_set_of_passed_in_points(self):
        liberties = [Point(5, 5), Point(5, 5)]
        go_string = GoString(Player.white, [], liberties)
        assert_that(go_string.liberties, equal_to({Point(5, 5)}))

    def test_remove_liberty_removes_passed_in_point_from_set(self):
        liberties = [Point(1, 2), Point(5, 5)]
        go_string = GoString(Player.white, [], liberties)
        go_string.remove_liberty(Point(1, 2))
        assert_that(go_string.liberties, equal_to({Point(5, 5)}))

    def test_add_liberty_add_passed_in_point_to_set(self):
        liberties = [Point(1, 2), Point(5, 5)]
        go_string = GoString(Player.white, [], [Point(5, 5)])
        go_string.add_liberty(Point(1, 2))
        assert_that(go_string.liberties, equal_to(set(liberties)))

    def test_merged_with_returns_go_string(self):
        go_string = GoString(Player.white, [], [])
        result = go_string.merged_with(GoString(Player.white, [], []))
        assert_that(result, instance_of(GoString))
