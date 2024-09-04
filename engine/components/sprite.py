from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from engine.gameobject import GameObject
from engine.component import Component
from enum import Enum
import pygame

SpriteRenderOrigin = Enum("SpriteRenderOrigin", ["TopLeft", "TopRight", "BottomLeft", "BottomRight", "Center"])

class Sprite(Component):
    def __init__(self, parent: GameObject, image: pygame.Surface = pygame.Surface((0, 0)), render_origin: SpriteRenderOrigin = SpriteRenderOrigin.Center, target_surface: pygame.Surface|None = None, scale: float = 1):
        super().__init__(parent)
        self.image = image
        self.render_origin = render_origin
        self.target_surface = target_surface if target_surface is not None else self.parent.scene.window_surface
        if scale != 1:
            self.image = pygame.transform.scale_by(self.image, scale)

    def update(self):
        self.target_surface.blit(self.image, self.parent.transform.get_offset_by_render_origin(self.render_origin, self.image).get_tuple())