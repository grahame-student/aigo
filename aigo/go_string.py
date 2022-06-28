from __future__ import annotations
from typing import List

from aigo.types.player import Player
from aigo.types.point import Point


class GoString:
    def __init__(self, colour: Player, stones: List[Point], liberties: List[Point]):
        self.colour = colour
        self.stones = set(stones)
        self.liberties = set(liberties)

    def remove_liberty(self, point: Point):
        self.liberties.remove(point)

    def add_liberty(self, point: Point):
        self.liberties.add(point)

    def merged_with(self, go_string: GoString) -> GoString:
        return GoString(Player.black, [], [])
