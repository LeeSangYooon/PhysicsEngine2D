import pygame
import sys
from core.Simulation import Simulation
from core.World import World
from core.DynamicObjects.Circle import Circle
from core.Vector2 import Vector2
from gui.Color import *
from examples.test import simulation
from copy import deepcopy
from typing import List


origin_world = deepcopy(simulation.world)

camera = Vector2(0, 0)
zoom = 40
frames = 0


pygame.init()

canvas_size = Vector2(1000, 1000)
screen = pygame.display.set_mode((canvas_size.x, canvas_size.y))
pygame.display.set_caption(simulation.title)
font_size = 32
font = pygame.font.SysFont("malgungothic", font_size)


def display_text(text, x, y):
    rendered_text = font.render(text, True, (0, 0, 0))  # Render the text with white color
    screen.blit(rendered_text, (x, y))  # Blit the rendered text onto the screen at the specified position

def display_multiline_text(texts:List[str]):
    for i in range(len(texts)):
        display_text(texts[i], 10, 10 + 40 * i)


def render_world(world: World):
    global frames
    screen.fill(WHITE)
    for obj in world.objects:
        if type(obj) is Circle:
            obj: Circle
            temp = (obj.position - camera) * zoom
            display_position = (temp.vertically_reversed() + canvas_size / 2).to_integer_pair()
            pygame.draw.circle(screen, obj.setting.color, display_position, obj.radius * zoom)
            text = f"{obj.mass}kg"
            half_text_length = (font_size // 4) * len(text)

            display_text(text, display_position[0] - half_text_length, display_position[1] - (font_size // 1.5))

    frames += 1
    display_multiline_text([
        f"시간: {simulation.world.time : .2f}초 (프레임: {frames})",
        f"{simulation.description}",
        f"총 운동량의 크기: {world.total_momentum().magnitude() : .2f}",
        f"총 운동 에너지의 크기: {world.total_kinematic_energy() : .2f}"
    ])


def update(world: World):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            pressed = pygame.key.get_pressed()
            if pressed[pygame.K_r]:
                simulation.world = deepcopy(origin_world)
                print("실험 재시작")
            if pressed[pygame.K_s]:
                simulation.stop = True
                print("실험 중단됨")

    render_world(world)
    pygame.display.flip()


def main():
    mode = None
    screen.fill(WHITE)
    display_text("실험 모드를 입력하세요 (1 또는 2 입력)", 10, 10)
    display_text("1: 정밀 실험 (오차 적음)", 10, 45)
    display_text("2: 실시간 실험 (실제 시간과 동일하게 시간 적용)", 10, 80)
    pygame.display.flip()
    while mode is None:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                pressed = pygame.key.get_pressed()
                if pressed[pygame.K_1]:
                    mode = 1
                    print("정밀 실험 시작")
                if pressed[pygame.K_2]:
                    mode = 2
                    print("실시간 실험 시작")
    if mode == 1:
        simulation.simulate_in_static_delta_time(delta_time=0.002, call_back=update)
    elif mode == 2:
        simulation.simulate_in_real_time(call_back=update)
    main()


if __name__ == '__main__':
    main()
