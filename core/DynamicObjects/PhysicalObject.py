from core.Vector2 import Vector2
from typing import List, Final
from core.DynamicObjects.ObjectSetting import ObjectSetting


class PhysicalObject:
    def __init__(self, mass: float, position=Vector2.ZERO, elastic_modulus=100.0, setting: ObjectSetting = None):
        self.mass: Final = mass
        self.velocity: Vector2 = Vector2.ZERO
        self.position = position
        self.forces: List[Vector2] = list()
        self.elastic_modulus = elastic_modulus
        self.setting = ObjectSetting() if setting is None else setting

    def net_power(self) -> Vector2:
        return Vector2.sum(self.forces)

    def acceleration(self):
        return self.net_power() / self.mass

    def momentum(self):
        return self.velocity * self.mass

    def kinematic_energy(self):
        return self.mass * (self.velocity.magnitude() ** 2)

    def add_force(self, force: Vector2):
        self.forces.append(force)
