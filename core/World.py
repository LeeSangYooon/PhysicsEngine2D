from core.DynamicObjects.PhysicalObject import PhysicalObject
from core.DynamicObjects.Circle import Circle
from core.StaticObjects.Wall import Wall
from core.Vector2 import Vector2
from typing import List, cast


class World:
    def __init__(self, gravity_scale=9.81):
        self.time: float = 0
        self.objects: List[PhysicalObject] = list()
        self.static_objects: List[Wall] = list()
        self.gravity_scale = gravity_scale

    def total_momentum(self) -> Vector2:
        return Vector2.sum(map(lambda x: x.momentum(), self.objects))

    def total_kinematic_energy(self) -> float:
        return sum(map(lambda x: x.kinematic_energy(), self.objects))

    def remove_forces(self):
        for obj in self.objects:
            if obj.setting.use_gravity:
                obj.forces.clear()

    def apply_gravity(self):
        for obj in self.objects:
            if obj.setting.use_gravity:
                gravity = Vector2.DOWN * self.gravity_scale * obj.mass
                obj.add_force(gravity)

    def apply_elasticity(self):
        for obj in self.objects:
            for static_obj in self.static_objects:
                pass

        for i in range(len(self.objects)):
            for j in range(i+1, len(self.objects)):
                a, b = self.objects[i], self.objects[j]
                if isinstance(a, Circle) and isinstance(b, Circle):
                    a = cast(Circle, a)
                    b = cast(Circle, b)
                    distance = (b.position - a.position).magnitude()
                    collided_distance = a.radius + b.radius - distance
                    if collided_distance <= 0:
                        continue
                    elasticity = collided_distance * a.elastic_modulus + collided_distance * b.elastic_modulus
                    a_force = (a.position - b.position).normalized() * elasticity
                    b_force = a_force * -1  # 작용 반작용
                    a.add_force(a_force)
                    b.add_force(b_force)
                else:
                    raise ValueError("아직 원과 원의 충돌만 구현함")

    def update(self, delta_time: float) -> None:
        # calculate forces
        self.remove_forces()
        self.apply_gravity()
        self.apply_elasticity()

        # calculate acceleration and position
        for obj in self.objects:
            obj.velocity += obj.acceleration() * delta_time
            obj.position += obj.velocity * delta_time

    def add_object(self, obj: PhysicalObject):
        self.objects.append(obj)

