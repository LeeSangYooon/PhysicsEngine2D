from core.Simulation import Simulation
from core.DynamicObjects.Circle import Circle
from core.Vector2 import Vector2
from core.DynamicObjects.ObjectSetting import ObjectSetting


simulation = Simulation()
for x, y in [(x, y) for x in range(-9, 8, 4) for y in range(-9, 8, 4)]:
    simulation.add_object(Circle(mass=1, radius=1, position=Vector2(x, y), elastic_modulus=1000))

wall_obj_setting = ObjectSetting(layer="Wall", static=True)
simulation.add_object(Circle(mass=1000000, radius=1000, elastic_modulus=10000, position=Vector2(-1011, 0), setting = wall_obj_setting))
simulation.add_object(Circle(mass=1000000, radius=1000, elastic_modulus=10000, position=Vector2(0, -1011), setting = wall_obj_setting))
simulation.add_object(Circle(mass=1000000, radius=1000, elastic_modulus=10000, position=Vector2(1011, 0), setting = wall_obj_setting))
simulation.add_object(Circle(mass=1000000, radius=1000, elastic_modulus=10000, position=Vector2(0, 1011), setting = wall_obj_setting))

simulation.world.ignore_layer.append("Wall")
simulation.world.objects[4].velocity = Vector2.LEFT * 30 + Vector2.UP * 5
simulation.world.gravity_scale = 9.81

simulation.title = "닫힌 공간"
simulation.description = "탄성 충돌을 함"
