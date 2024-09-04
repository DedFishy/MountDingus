from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from engine.gameobject import GameObject

class Component:
    def __init__(self, parent: GameObject):
        self.parent = parent

    def update(self):
        pass