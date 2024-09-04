from typing import Callable
from engine.component import Component
from engine.gameobject import GameObject


class Restrictor(Component):
    def __init__(self, parent: GameObject, anchor_x: bool = False, anchor_y: bool = False):
        super().__init__(parent)
        self.anchor_x = anchor_x
        self.anchor_y = anchor_y

    def update(self):
        if self.anchor_x:
            self.parent.transform.center_in_container_absolute_x(int(self.parent.scene.window_surface.width / 2))
        if self.anchor_y:
            self.parent.transform.center_in_container_absolute_y(int(self.parent.scene.window_surface.height / 2))