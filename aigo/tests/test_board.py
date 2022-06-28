from unittest import TestCase

from aigo.board import Board
from aigo.go_string import GoString
from aigo.types.player import Player
from aigo.types.point import Point
from hamcrest import assert_that, calling, equal_to, instance_of, raises


class TestBoard(TestCase):
    def test_constructor_sets_rows_to_passed_in_size(self):
        board = Board(123, 0)
        assert_that(board.rows, equal_to(123))

    def test_constructor_sets_cols_to_passed_in_size(self):
        board = Board(0, 123)
        assert_that(board.cols, equal_to(123))

    def test_place_stone_throws_exception_if_point_row_greater_than_grid_row(self):
        board = Board(5, 5)
        assert_that(calling(board.place_stone).with_args(Player.white, Point(6, 3)), raises(Exception))

    def test_place_stone_throws_exception_if_point_row_less_than_grid_row(self):
        board = Board(5, 5)
        assert_that(calling(board.place_stone).with_args(Player.white, Point(0, 3)), raises(Exception))

    def test_place_stone_throws_exception_if_point_col_greater_than_grid_col(self):
        board = Board(5, 5)
        assert_that(calling(board.place_stone).with_args(Player.white, Point(3, 6)), raises(Exception))

    def test_place_stone_throws_exception_if_point_col_less_than_grid_col(self):
        board = Board(5, 5)
        assert_that(calling(board.place_stone).with_args(Player.white, Point(3, 0)), raises(Exception))

    def test_place_stone_throws_exception_if_point_already_played(self):
        board = Board(5, 5)
        board.place_stone(Player.white, Point(1, 1))
        assert_that(calling(board.place_stone).with_args(Player.white, Point(1, 1)), raises(Exception))

    def test_place_stone_adds_neighbours_to_liberties(self):
        board = Board(5, 5)
        board.place_stone(Player.white, Point(3, 3))
        string = board.get_go_string(Point(3, 3))
        expected_liberties = {Point(2, 3), Point(4, 3), Point(3, 2), Point(3, 4)}
        assert_that(string.liberties, equal_to(expected_liberties))

    def test_place_stone_only_adds_neighbours_on_grid_to_liberties(self):
        board = Board(5, 5)
        board.place_stone(Player.white, Point(3, 1))
        string = board.get_go_string(Point(3, 1))
        expected_liberties = {Point(2, 1), Point(4, 1), Point(3, 2)}
        assert_that(string.liberties, equal_to(expected_liberties))

    def test_place_stone_adds_unclaimed_neighbours_to_liberties(self):
        board = Board(5, 5)
        board.place_stone(Player.black, Point(2, 3))
        board.place_stone(Player.white, Point(3, 3))
        string = board.get_go_string(Point(3, 3))
        expected_liberties = {Point(4, 3), Point(3, 2), Point(3, 4)}
        assert_that(string.liberties, equal_to(expected_liberties))

    # adding a stone next to other player's stone should remove a liberty from other player's stone
    #  .      .
    # .o. -> .ox
    #  .      .

    def test_get_go_string_returns_none_if_point_unclaimed(self):
        board = Board(5, 5)
        assert_that(board.get_go_string(Point(1, 1)), equal_to(None))

    def test_get_go_string_returns_go_string_if_point_claimed(self):
        board = Board(5, 5)
        board.place_stone(Player.white, Point(1, 1))
        assert_that(board.get_go_string(Point(1, 1)), instance_of(GoString))
