from __future__ import annotations
from enum import Enum
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from engine.window import Window
    from engine.gameobject import GameObject

import pygame

TransitionReason = Enum("TransitionReason", ["INITIAL_SCENE"])

class Scene:
    """Defines a separate part of the game.
    Note that __init__ should be called before anything, and transition should be called before setting the scene as the one rendered.
    Initialization should be done in transition to ensure the scene can be reused."""

    BACKGROUND_COLOR = pygame.Color(100, 100, 100)

    def __init__(self, window: Window):
        self.window = window
        self.window_surface = window.window
        self.gameobjects: list[GameObject] = []

    def transition(self, origin: Scene|TransitionReason, **kwargs):
        pass

    def update(self):
        for object in self.gameobjects:
            object.update()