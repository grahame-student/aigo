from unittest import TestCase

from aigo.go_string import GoString
from aigo.types.player import Player
from aigo.types.point import Point
from hamcrest import assert_that, calling, equal_to, instance_of, raises


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

    def test_merged_with_sets_colour_to_colour(self):
        go_string = GoString(Player.white, [Point(1, 1)], [])
        result = go_string.merged_with(GoString(Player.white, [Point(2, 2)], []))
        assert_that(result.colour, equal_to(Player.white))

    def test_merged_with_throws_exception_when_colours_different(self):
        go_string = GoString(Player.black, [Point(1, 1)], [])
        assert_that(
            calling(go_string.merged_with).with_args(
                GoString(Player.white, [Point(2, 2)], [])
            ),
            raises(Exception),
        )

    def test_merged_with_sets_stones_to_combined_list_of_stones(self):
        go_string = GoString(Player.white, [Point(1, 1)], [])
        result = go_string.merged_with(GoString(Player.white, [Point(2, 2)], []))
        assert_that(result.stones, equal_to({Point(1, 1), Point(2, 2)}))

    def test_merged_with_sets_liberties_to_combined_list_of_liberties(self):
        go_string = GoString(Player.white, [], [Point(1, 1)])
        result = go_string.merged_with(GoString(Player.white, [], [Point(2, 2)]))
        assert_that(result.liberties, equal_to({Point(1, 1), Point(2, 2)}))

    def test_merged_with_removed_combined_stones_from_combined_list_of_liberties(self):
        go_string = GoString(Player.white, [], [Point(1, 1)])
        result = go_string.merged_with(
            GoString(Player.white, [Point(1, 1)], [Point(2, 2)])
        )
        assert_that(result.liberties, equal_to({Point(2, 2)}))

    def test_num_liberties_returns_liberties_in_set(self):
        liberties = [Point(1, 2), Point(5, 5)]
        go_string = GoString(Player.white, [], liberties)
        assert_that(go_string.num_liberties, equal_to(2))

    def test_equality_returns_true_when_other_instance_is_go_string(self):
        go_string = GoString(Player.black, [], [])
        other = GoString(Player.black, [], [])
        assert_that(go_string == other, equal_to(True))

    def test_equality_returns_false_when_other_instance_is_not_go_string(self):
        go_string = GoString(Player.black, [], [])
        other = None
        assert_that(go_string == other, equal_to(False))

    def test_equality_returns_true_when_colour_equals_other_colour(self):
        go_string = GoString(Player.black, [], [])
        other = GoString(Player.black, [], [])
        assert_that(go_string == other, equal_to(True))

    def test_equality_returns_false_when_colour_not_equal_to_other_colour(self):
        go_string = GoString(Player.white, [], [])
        other = GoString(Player.black, [], [])
        assert_that(go_string == other, equal_to(False))

    def test_equality_returns_true_when_stones_equals_other_stones(self):
        stones = [Point(1, 1)]
        go_string = GoString(Player.black, stones, [])
        other = GoString(Player.black, stones, [])
        assert_that(go_string == other, equal_to(True))

    def test_equality_returns_false_when_stones_not_equal_to_other_stones(self):
        stones = [Point(1, 1)]
        go_string = GoString(Player.black, stones, [])
        other = GoString(Player.black, [], [])
        assert_that(go_string == other, equal_to(False))

    def test_equality_returns_true_when_liberties_equals_other_liberties(self):
        liberties = [Point(1, 1)]
        go_string = GoString(Player.black, [], liberties)
        other = GoString(Player.black, [], liberties)
        assert_that(go_string == other, equal_to(True))

    def test_equality_returns_false_when_liberties_not_equal_to_other_liberties(self):
        liberties = [Point(1, 1)]
        go_string = GoString(Player.black, [], liberties)
        other = GoString(Player.black, [], [])
        assert_that(go_string == other, equal_to(False))
