from core.DynamicObjects.PhysicalObject import PhysicalObject
from core.Vector2 import Vector2
from core.DynamicObjects.ObjectSetting import ObjectSetting
from typing import Final


class Circle(PhysicalObject):
    def __init__(self, mass: float, radius: float, position=Vector2.ZERO, elastic_modulus=100.0, setting: ObjectSetting = None):
        super().__init__(mass, position, elastic_modulus, setting)
        self.radius: Final = radius
