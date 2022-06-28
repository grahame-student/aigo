from unittest import TestCase

from aigo.board import Board

from hamcrest import assert_that, equal_to


class TestBoard(TestCase):
    def test_constructor_sets_rows_to_passed_in_size(self):
        board = Board(123, 0)
        assert_that(board.rows, equal_to(123))

    def test_constructor_sets_cols_to_passed_in_size(self):
        board = Board(0, 123)
        assert_that(board.cols, equal_to(123))
