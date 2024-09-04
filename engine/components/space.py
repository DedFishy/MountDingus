import pymunk
from engine.component import Component
from engine.gameobject import GameObject


class Space(Component):
    def __init__(self, parent: GameObject, gravity: tuple = (0, 0)):
        super().__init__(parent)
        self.space = pymunk.Space()
        self.space.gravity = gravity

    

    def update(self):
        deltatime = self.parent.scene.window.deltatime
        steps = 10
        step_total = deltatime * 1000
        for _ in range(steps):
            self.space.step(step_total/steps)