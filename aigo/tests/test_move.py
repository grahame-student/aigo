from unittest import TestCase

from aigo.move import Move
from aigo.types.point import Point
from hamcrest import assert_that, calling, equal_to, raises


class TestMove(TestCase):
    def test_play_sets_point_to_passed_in_point(self):
        move = Move.play(Point(5, 5))
        assert_that(move.point, equal_to(Point(5, 5)))

    def test_play_sets_is_pass_to_false(self):
        move = Move.play(Point(5, 5))
        assert_that(move.is_pass, equal_to(False))

    def test_play_sets_is_resign_to_false(self):
        move = Move.play(Point(5, 5))
        assert_that(move.is_resign, equal_to(False))

    def test_play_sets_is_play_to_true(self):
        move = Move.play(Point(5, 5))
        assert_that(move.is_play, equal_to(True))

    def test_pass_turn_sets_point_to_none(self):
        move = Move.pass_turn()
        assert_that(move.point, equal_to(None))

    def test_pass_turn_sets_is_pass_to_true(self):
        move = Move.pass_turn()
        assert_that(move.is_pass, equal_to(True))

    def test_pass_turn_sets_is_resign_to_false(self):
        move = Move.pass_turn()
        assert_that(move.is_resign, equal_to(False))

    def test_pass_turn_sets_is_play_to_false(self):
        move = Move.pass_turn()
        assert_that(move.is_play, equal_to(False))

    def test_resign_sets_point_to_none(self):
        move = Move.resign()
        assert_that(move.point, equal_to(None))

    def test_resign_sets_is_pass_to_false(self):
        move = Move.resign()
        assert_that(move.is_pass, equal_to(False))

    def test_resign_sets_is_resign_to_true(self):
        move = Move.resign()
        assert_that(move.is_resign, equal_to(True))

    def test_resign_sets_is_play_to_false(self):
        move = Move.resign()
        assert_that(move.is_play, equal_to(False))

    def test_constructor_raises_exception_when_multiple_arguments_set(self):
        move = Move(None, True)
        assert_that(calling(move.__init__).with_args(Point(5, 5), True), raises(Exception))
