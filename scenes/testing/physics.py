import pygame
from engine.components.animator import Animator, ease_out_cubic
from engine.components.restrictor import Restrictor
from engine.components.sprite import Sprite
from engine.gameobject import GameObject
from engine.scene import Scene, TransitionReason

class Physics(Scene):
    def __init__(self, window):
        super().__init__(window)

        self.space = GameObject(self, 0, 0)

        self.ball = GameObject(self, 0, 0)
        self.ball.set_components({
            })
        self.gameobjects.append(self.ball)

    def transition(self, origin: Scene | TransitionReason, **kwargs):
        super().transition(origin, **kwargs)

    def update(self):
        super().update()