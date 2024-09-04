from __future__ import annotations
from typing import Callable
from engine.component import Component
import time



class Animator(Component):
    def __init__(self, animation_time: float, start_value: float, end_value: float, set_target_value: Callable[[float]], animation_equation: Callable[[Animator], float]):
        self.current_time = 0.0
        self.animation_time = animation_time
        self.start_value = start_value
        self.end_value = end_value
        self.change = self.end_value - self.start_value
        self.set_target_value = set_target_value

        self.animation_started_time = None # Set when the animation is started

        self.animation_equation = animation_equation

    def start(self):
        self.animation_started_time = time.time()

    def normalized_animation_time(self):
        return self.current_time / self.animation_time

    def normalized_value_to_physical_value(self, normalized_value: float) -> float:
        return self.start_value + (normalized_value * self.change)

    def get_current_animation_value(self) -> float:
        if not self.animation_started_time: raise AttributeError("Animation not started before getting value!")
        return self.animation_equation(self)

    def update(self) -> bool:
        if not self.animation_started_time: raise AttributeError("Animation not started before updating! Have you called start() on this Animator?")

        self.current_time = time.time() - self.animation_started_time

        current_value = self.get_current_animation_value()
        real_val = self.normalized_value_to_physical_value(current_value)
        self.set_target_value(real_val)
        if real_val <= self.end_value:
            self.set_target_value(self.end_value)
            return False
        return True

def ease_out_cubic(animator: Animator):
    return 1 - ((1 - animator.normalized_animation_time())**3)