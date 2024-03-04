from __future__ import annotations
from dataclasses import dataclass
from enum import Enum


@dataclass(frozen=True)
class Point:
    """(x, y) point on the grid."""

    x: int
    y: int

    def __add__(self, other: Point | Vector) -> Point | Vector:
        if isinstance(other, Point):
            diff_x = self.x + other.x
            diff_y = self.y + other.y
            return Vector(diff_x, diff_y)
        elif isinstance(other, Vector):
            diff_x = self.x + other.run
            diff_y = self.y + other.rise
            return Point(diff_x, diff_y)
    
    def __sub__(self, other: Point | Vector) -> Point | Vector:
        if isinstance(other, Point):
            diff_x = self.x - other.x
            diff_y = self.y - other.y
            return Vector(diff_x, diff_y)
        elif isinstance(other, Vector):
            diff_x = self.x - other.run
            diff_y = self.y - other.rise
            return Point(diff_x, diff_y)
    
    def __eq__(self, other: Point) -> bool:
        return self.x == other.x and self.y == other.y


@dataclass(frozen=True)
class Vector:
    """(d_x, d_y) vector on the grid."""

    run: int
    rise: int

    def __mul__(self, other: int) -> Vector:
        return Vector(self.run * other, self.rise * other)
    
    def __eq__(self, other: Vector) -> bool:
        return self.run == other.run and self.rise == other.rise


class Direction(Enum):
    """Possible directions for snake to travel in."""

    N = Vector(0, -1)
    E = Vector(1, 0)
    S = Vector(0, 1)
    W = Vector(-1, 0)