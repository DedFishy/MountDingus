from enum import Enum
from typing import Any, Callable
import pymunk
from engine.component import Component
from engine.gameobject import GameObject


class RigidBody(Component):
    def __init__(self, parent: GameObject, body_type: int = pymunk.Body.DYNAMIC):
        super().__init__(parent)

        self.body = pymunk.Body(body_type=body_type)
        self.body.position = self.parent.transform.get_tuple()

    def add_collider(self, collider_constructor: Callable[..., pymunk.Poly], extra_args: tuple = (), extra_kwargs: dict = {}):
        poly = collider_constructor(self.body, *extra_args, **extra_kwargs)
        poly
        return poly

    def _update_parent_position(self):
        self.parent.transform.set_tuple(self.body.position)

    def update(self):
        self._update_parent_position()