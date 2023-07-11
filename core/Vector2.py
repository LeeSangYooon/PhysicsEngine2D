from typing import Self, Final, List, Tuple
from math import sqrt


class Vector2:
    ZERO: Self
    UP: Self
    DOWN: Self
    RIGHT: Self
    LEFT: Self

    def __init__(self, x: float, y: float) -> None:
        self.x: Final = x
        self.y: Final = y

    def magnitude(self):
        return sqrt(pow(self.x, 2) + pow(self.y, 2))

    def normalized(self):
        magnitude = self.magnitude()
        return Vector2(self.x / magnitude, self.y / magnitude)

    def to_integer_pair(self) -> Tuple[int, int]:
        return round(self.x), round(self.y)

    def vertically_reversed(self):
        return Vector2(self.x, -self.y)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __add__(self, other: Self):
        return Vector2(self.x + other.x, self.y + other.y)

    def __sub__(self, other: Self):
        return Vector2(self.x - other.x, self.y - other.y)

    def __mul__(self, other: float):
        return Vector2(self.x * other, self.y * other)

    def __truediv__(self, other: float):
        return Vector2(self.x / other, self.y / other)

    def __str__(self):
        return f"Vector2 X: {self.x} Y: {self.y}"

    @staticmethod
    def sum(force_list: List['Vector2']):
        return sum(force_list, Vector2.ZERO)


Vector2.ZERO = Vector2(0, 0)
Vector2.UP = Vector2(0, 1)
Vector2.DOWN = Vector2(0, -1)
Vector2.RIGHT = Vector2(1, 0)
Vector2.LEFT = Vector2(-1, 0)
