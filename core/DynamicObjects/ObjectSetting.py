from gui.Color import random_color


class ObjectSetting:
    def __init__(self, use_gravity=True, color=None, static=False, layer="Default"):
        self.use_gravity: bool = use_gravity
        self.color = random_color() if color is None else color
        self.static = static
        self.layer = layer
