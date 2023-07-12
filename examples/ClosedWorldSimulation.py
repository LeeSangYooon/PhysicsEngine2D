from core.Simulation import Simulation
from core.DynamicObjects.Circle import Circle
from core.Vector2 import Vector2
from core.DynamicObjects.ObjectSetting import ObjectSetting


simulation = Simulation()
simulation.add_object(Circle(mass=1, radius=1, position=Vector2(-10, 0)))
simulation.add_object(Circle(mass=1, radius=1, position=Vector2(-5, 0)))
simulation.add_object(Circle(mass=1, radius=1, position=Vector2(0, 0)))
simulation.add_object(Circle(mass=1, radius=1, position=Vector2(5, 0)))
simulation.add_object(Circle(mass=1, radius=1, position=Vector2(10, 0.02)))
simulation.add_object(Circle(mass=1, radius=1, position=Vector2(-10, 5)))
simulation.add_object(Circle(mass=1, radius=1, position=Vector2(-5, 5)))
simulation.add_object(Circle(mass=1, radius=1, position=Vector2(0, 5)))
simulation.add_object(Circle(mass=1, radius=1, position=Vector2(5, 5)))
simulation.add_object(Circle(mass=1, radius=1, position=Vector2(10, 5)))
simulation.add_object(Circle(mass=1, radius=1, position=Vector2(-10, -5)))
simulation.add_object(Circle(mass=1, radius=1, position=Vector2(-5, -5)))
simulation.add_object(Circle(mass=1, radius=1, position=Vector2(0, -5)))
simulation.add_object(Circle(mass=1, radius=1, position=Vector2(5, -5)))
simulation.add_object(Circle(mass=1, radius=1, position=Vector2(10, -5)))

wall_obj_setting = ObjectSetting(layer="Wall", static=True)
simulation.add_object(Circle(mass=1000000, radius=1000, elastic_modulus=10000, position=Vector2(-1011, 0), setting = wall_obj_setting))
simulation.add_object(Circle(mass=1000000, radius=1000, elastic_modulus=10000, position=Vector2(0, -1011), setting = wall_obj_setting))
simulation.add_object(Circle(mass=1000000, radius=1000, elastic_modulus=10000, position=Vector2(1011, 0), setting = wall_obj_setting))
simulation.add_object(Circle(mass=1000000, radius=1000, elastic_modulus=10000, position=Vector2(0, 1011), setting = wall_obj_setting))

simulation.world.ignore_layer.append("Wall")
simulation.world.objects[4].velocity = Vector2.LEFT * 30 + Vector2.UP * 5
simulation.world.gravity_scale = 9.81
