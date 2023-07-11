from core.Objects.PhysicalObject import PhysicalObject
from core.Vector2 import Vector2
from typing import List


class World:
    def __init__(self, gravity_scale=9.81):
        self.time: float = 0
        self.objects: List[PhysicalObject] = list()
        self.gravity_scale = gravity_scale

    def remove_forces(self):
        for obj in self.objects:
            if obj.setting.use_gravity:
                obj.forces.clear()

    def apply_gravity(self):
        for obj in self.objects:
            if obj.setting.use_gravity:
                gravity = Vector2.DOWN * self.gravity_scale * obj.mass
                obj.add_force(gravity)

    def update(self, delta_time: float) -> None:
        # calculate forces
        self.remove_forces()
        self.apply_gravity()

        # calculate acceleration and position
        for obj in self.objects:
            obj.velocity += obj.acceleration() * delta_time
            obj.position += obj.velocity * delta_time

    def add_object(self, obj: PhysicalObject):
        self.objects.append(obj)

