from gui.Color import random_color


class ObjectSetting:
    def __init__(self, use_gravity=True, color=random_color()):
        self.use_gravity: bool = use_gravity
        self.color = color
