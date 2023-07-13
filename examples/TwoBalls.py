from core.Simulation import Simulation
from core.DynamicObjects.Circle import Circle
from core.Vector2 import Vector2
from core.DynamicObjects.ObjectSetting import ObjectSetting


simulation = Simulation()
simulation.add_object(Circle(mass=3, radius=3, position=Vector2(0, 0), elastic_modulus=1000))
simulation.add_object(Circle(mass=1, radius=1, position=Vector2(0, 4), elastic_modulus=1000))

wall_obj_setting = ObjectSetting(layer="Wall", static=True)
simulation.add_object(Circle(mass=1000000, radius=1000, elastic_modulus=10000, position=Vector2(0, -1011), setting = wall_obj_setting))
simulation.world.ignore_layer.append("Wall")

simulation.world.gravity_scale = 9.81

simulation.title = "공 떨어뜨리기"
simulation.description = "공 떨어뜨리기 실험"
