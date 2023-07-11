from core.World import World
from core.DynamicObjects.PhysicalObject import PhysicalObject
from time import time
from typing import Callable
from math import inf as INF


class Simulation:
    def __init__(self, world: World = World()):
        self.world = world
        self.time = 0

    def simulate_in_real_time(self, time_limit=INF, call_back: Callable[[World], None] = None):
        self.time = time()
        while self.time < time_limit:
            now_time = time()
            delta_time = now_time - self.time
            self.time = now_time

            self.world.update(delta_time)
            if call_back is not None:
                call_back(self.world)

    def simulate_in_static_delta_time(self, delta_time: float, total_frame=INF,
                                      call_back: Callable[[World], None] = None) -> None:
        n = 0
        while n < total_frame:
            self.world.update(delta_time)
            if call_back is not None:
                call_back(self.world)

    def add_object(self, obj: PhysicalObject):
        self.world.add_object(obj)

