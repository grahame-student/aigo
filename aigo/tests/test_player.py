from unittest import TestCase

from aigo.player import Player
from hamcrest import assert_that, equal_to


class TestPlayer(TestCase):
    def test_other_returns_black_when_player_is_white(self):
        player = Player.white
        assert_that(player.other, equal_to(Player.black))

    def test_other_returns_white_when_player_is_black(self):
        player = Player.black
        assert_that(player.other, equal_to(Player.white))
