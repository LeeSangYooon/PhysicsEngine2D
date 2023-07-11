from core.Vector2 import Vector2
from typing import List, Final
from core.DynamicObjects.ObjectSetting import ObjectSetting


class PhysicalObject:
    def __init__(self, mass: float, position=Vector2.ZERO, setting: ObjectSetting = ObjectSetting()):
        self.mass: Final = mass
        self.velocity: Vector2 = Vector2.ZERO
        self.position = position
        self.forces: List[Vector2] = list()
        self.setting = setting

    def net_power(self) -> Vector2:
        return Vector2.sum(self.forces)

    def acceleration(self):
        return self.net_power() / self.mass

    def add_force(self, force: Vector2):
        self.forces.append(force)
