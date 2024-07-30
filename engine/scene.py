from __future__ import annotations
from enum import Enum

TransitionReason = Enum("TransitionReason", ["INITIAL_SCENE"])

class Scene:
    """Defines a separate part of the game.
    Note that __init__ should be called before anything, and transition should be called """
    def __init__(self):
        pass

    def transition(self, origin: Scene|TransitionReason, **kwargs):
        pass