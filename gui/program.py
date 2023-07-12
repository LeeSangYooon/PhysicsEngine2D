import pygame
import sys
from core.Simulation import Simulation
from core.World import World
from core.DynamicObjects.Circle import Circle
from core.Vector2 import Vector2
from gui.Color import *


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
simulation.world.objects[4].velocity = Vector2.LEFT * 30
simulation.world.gravity_scale = 0

camera = Vector2(0, 0)
zoom = 40
frames = 0


pygame.init()

canvas_size = Vector2(1000, 1000)
screen = pygame.display.set_mode((canvas_size.x, canvas_size.y))
pygame.display.set_caption("2D Physics Engine")
font = pygame.font.Font(None, 28)


def display_text(text, x, y):
    rendered_text = font.render(text, True, (255, 255, 255))  # Render the text with white color
    screen.blit(rendered_text, (x, y))  # Blit the rendered text onto the screen at the specified position


def render_world(world: World):
    global frames
    screen.fill(WHITE)
    for obj in world.objects:
        if type(obj) is Circle:
            obj: Circle
            display_position = (obj.position - camera) * zoom
            display_position = display_position.vertically_reversed() + canvas_size / 2
            pygame.draw.circle(screen, obj.setting.color, display_position.to_integer_pair(), obj.radius * zoom)
    frames += 1
    display_text(f"#frame {frames}", 10, 10)
    display_text(f"총 운동량: {world.total_momentum().magnitude()}", 10, 40)
    display_text(f"총 운동 에너지: {world.total_kinematic_energy()}", 10, 70)


def update(world: World):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    render_world(world)
    pygame.display.flip()


def main():
    simulation.simulate_in_real_time(call_back=update)


if __name__ == '__main__':
    main()
