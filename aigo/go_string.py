from __future__ import annotations
from typing import List, Union, Set

from aigo.types.player import Player
from aigo.types.point import Point


class GoString:
    def __init__(self, colour: Player, stones: Union[List[Point], Set[Point]], liberties: Union[List[Point], Set[Point]]):
        self.colour = colour
        self.stones = set(stones)
        self.liberties = set(liberties)

    def __eq__(self, other):
        return isinstance(other, GoString) and \
               self.colour == other.colour and \
               self.stones == other.stones and \
               self.liberties == other.liberties

    @property
    def num_liberties(self):
        return len(self.liberties)

    def remove_liberty(self, point: Point):
        self.liberties.remove(point)

    def add_liberty(self, point: Point):
        self.liberties.add(point)

    def merged_with(self, go_string: GoString) -> GoString:
        assert self.colour == go_string.colour
        combined_stones = self.stones | go_string.stones
        combined_liberties = (self.liberties | go_string.liberties) - combined_stones
        return GoString(self.colour, combined_stones, combined_liberties)
