from core.Simulation import Simulation
from core.DynamicObjects.Circle import Circle
from core.Vector2 import Vector2


simulation = Simulation()
simulation.add_object(Circle(mass=1, radius=1, position=Vector2(0, 0), elastic_modulus=100))
simulation.add_object(Circle(mass=1, radius=1, position=Vector2(10, 1), elastic_modulus=100))

simulation.world.objects[1].velocity = Vector2.LEFT * 5

simulation.world.gravity_scale = 0

simulation.title = "탄성 충돌"
simulation.description = "동일한 질량을 가진 물체 탄성 충돌"
