from core.Simulation import Simulation
from core.DynamicObjects.Circle import Circle
from core.Vector2 import Vector2


simulation = Simulation()
simulation.add_object(Circle(mass=1, radius=1, position=Vector2(-10, 0)))
simulation.add_object(Circle(mass=1, radius=1, position=Vector2(-5, 0)))
simulation.add_object(Circle(mass=1, radius=1, position=Vector2(0, 0)))
simulation.add_object(Circle(mass=1, radius=1, position=Vector2(5, 0)))
simulation.add_object(Circle(mass=1, radius=1, position=Vector2(10, 0)))

simulation.world.objects[4].velocity = Vector2.LEFT * 5

simulation.world.gravity_scale = 0

simulation.title = "탄성 충돌"
simulation.description = "동일한 질량을 가진 물체 탄성 충돌"
