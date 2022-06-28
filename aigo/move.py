from __future__ import annotations
from typing import Optional

from aigo.types.point import Point


class Move:
    def __init__(
        self,
        point: Point = None,
        is_pass: bool = False,
        is_resign: bool = False,
    ):
        point_set = point is not None
        assert point_set ^ is_pass ^ is_resign
        self.point = point
        self.is_play = point is not None
        self.is_pass = is_pass
        self.is_resign = is_resign

    @classmethod
    def play(cls, point) -> Move:
        return Move(point=point)

    @classmethod
    def pass_turn(cls) -> Move:
        return Move(is_pass=True)

    @classmethod
    def resign(cls) -> Move:
        return Move(is_resign=True)
