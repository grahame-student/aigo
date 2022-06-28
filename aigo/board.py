from typing import List, Union

from aigo.go_string import GoString
from aigo.types.player import Player
from aigo.types.point import Point


class Board:
    def __init__(self, rows, cols):
        self.cols = cols
        self.rows = rows
        self.__grid = {}

    def place_stone(self, player: Player, point: Point):
        assert self.__is_on_grid(point)
        assert self.__get(point) is None
        liberties: List[Point] = []
        for neighbour in point.neighbours():
            if not self.__is_on_grid(neighbour):
                continue
            neighbour_string = self.__get(neighbour)
            if neighbour_string is None:
                liberties.append(neighbour)

        new_string = GoString(player, [point], liberties)
        for go_string_point in new_string.stones:
            self.__grid[go_string_point] = new_string

    def __is_on_grid(self, point: Point) -> bool:
        return 1 <= point.row <= self.rows and 1 <= point.col <= self.cols

    def __get(self, point) -> Union[Player, None]:
        string = self.__grid.get(point)
        return None if string is None else string.colour

    def get_go_string(self, point: Point) -> Union[GoString, None]:
        string = self.__grid.get(point)
        return None if string is None else string
