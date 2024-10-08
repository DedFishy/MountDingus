import pygame
from engine.components.animator import Animator, ease_out_cubic
from engine.components.restrictor import Restrictor
from engine.components.sprite import Sprite
from engine.gameobject import GameObject
from engine.scene import Scene, TransitionReason

class MainMenu(Scene):
    def __init__(self, window):
        super().__init__(window)

        # Title
        self.title = GameObject(self, 0, 0)
        self.title.set_components({
            "sprite": Sprite(self.title, pygame.image.load("assets/title.png")),
            "center": Restrictor(self.title, True, False),
            "fly_in_animator": Animator(3, 1000, 0, self.title.transform.set_y, ease_out_cubic)
            })
        self.gameobjects.append(self.title)

    def transition(self, origin: Scene | TransitionReason, **kwargs):
        super().transition(origin, **kwargs)
        animator: Animator = self.title.get_component("fly_in_animator")
        animator.start()

    def update(self):
        super().update()