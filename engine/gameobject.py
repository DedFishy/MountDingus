from typing import Any
from engine.math import Transform
from engine.component import Component
from engine.scene import Scene


class GameObject:
    def __init__(self, scene: Scene, x: int = 0, y: int = 0):
        self.scene = scene
        self.components = {}
        self.transform = Transform(x, y)

    def add_component(self, name: str, component: Component):
        self.components[name] = component

    def set_components(self, components: dict[str, Component]):
        self.components = components

    def try_get_component(self, component: str) -> Any:
        try:
            return self.get_component(component)
        except KeyError:
            return None

    def get_component(self, component: str) -> Any:
        component_found = self.components[component]
        return component_found

    def update(self):
        components_to_finish = []
        for component in self.components.keys():
            result = self.components[component].update()
            if result == False:
                components_to_finish.append(component)
        for component in components_to_finish:
            del self.components[component]
