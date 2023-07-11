import pygame
import sys
from core.Simulation import Simulation
from core.World import World
from core.Objects.Circle import Circle
from core.Vector2 import Vector2
from gui.Color import *


simulation = Simulation()
simulation.add_object(Circle(mass=100, radius=0.3, position=Vector2(-2.5, 2.5)))
simulation.add_object(Circle(mass=1, radius=0.3, position=Vector2(2.5, 2.5)))
simulation.world.objects[1].velocity = Vector2.UP * 3

camera = Vector2(0, 0)
zoom = 160
frames = 0


pygame.init()

canvas_size = Vector2(1600, 1200)
screen = pygame.display.set_mode((canvas_size.x, canvas_size.y))
pygame.display.set_caption("2D Physics Engine")


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
    print(f"#frame {frames}")


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
