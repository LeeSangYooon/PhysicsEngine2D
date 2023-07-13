from core.DynamicObjects.PhysicalObject import PhysicalObject
from core.DynamicObjects.Circle import Circle
from core.StaticObjects.Wall import Wall
from core.Vector2 import Vector2
from typing import List, cast


class World:
    def __init__(self, gravity_scale=9.81, ignore_layer: List[str] = None):
        self.time: float = 0
        self.objects: List[PhysicalObject] = list()
        self.static_objects: List[Wall] = list()
        self.gravity_scale = gravity_scale
        if ignore_layer is None:
            self.ignore_layer: List[str] = []
        else:
            self.ignore_layer = ignore_layer

    def total_momentum(self) -> Vector2:
        return Vector2.sum(map(lambda x: x.momentum(), self.objects))

    def total_kinematic_energy(self) -> float:
        return sum(map(lambda x: x.kinematic_energy(), self.objects))

    def remove_forces(self):
        for obj in self.objects:
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
            a = self.objects[i]
            for j in range(i+1, len(self.objects)):
                b = self.objects[j]
                if isinstance(a, Circle) and isinstance(b, Circle):
                    if a.setting.layer == b.setting.layer and a.setting.layer in self.ignore_layer:
                        continue
                    a = cast(Circle, a)  # 물체 A
                    b = cast(Circle, b)  # 물체 B
                    distance = (b.position - a.position).magnitude()  # D (거리)
                    collided_distance = a.radius + b.radius - distance  # RA + RB - D
                    if collided_distance <= 0:  # 만약 닿은 거리가 0보다 작다면 닿지 않은 것이다.
                        continue
                    elasticity = collided_distance * a.elastic_modulus + collided_distance * b.elastic_modulus  # (KA + KB) * (RA + RB - D)
                    a_force = (a.position - b.position).normalized() * elasticity  # B가 A를 보는 방향
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
            if obj.setting.static:
                continue
            obj.velocity += obj.acceleration() * delta_time
            obj.position += obj.velocity * delta_time
        self.time += delta_time

    def add_object(self, obj: PhysicalObject):
        self.objects.append(obj)

