from core.Vector2 import Vector2
from typing import Final


# ax + by + c > 0
class Wall:
    def __init__(self, pivot: Vector2, direction: Vector2):
        d = direction
        # d 의 오른쪽 방향 면이 벽이다.
        # 벽에 해당 하는 부등식
        if d == Vector2.RIGHT:
            # 벽: y < pos.y
            self.a = 0
            self.b = -1
            self.c = pivot.y
        elif d == Vector2.LEFT:
            # 벽: y > pos.y
            self.a = 0
            self.b = 1
            self.c = -pivot.y
        elif d == Vector2.UP:
            # 벽: x > pos.x
            self.a = 1
            self.b = 0
            self.c = -pivot.x
        elif d == Vector2.DOWN:
            # 벽: x < pos.x
            self.a = -1
            self.b = 0
            self.c = pivot.x
        else:
            inclination = direction.y / direction.x
            self.a = inclination
            self.b = -1
            self.c = -inclination * pivot.x + pivot.y

        self.pivot: Final = pivot
        self.direction: Final = d
