from __future__ import annotations
from typing import TYPE_CHECKING
from engine.components.sprite import SpriteRenderOrigin
import pygame

class Transform:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def set_x(self, x: int|float): self.x = int(x)
    def set_y(self, y: int|float): self.y = int(y)

    def get_tuple(self) -> tuple: return (self.x, self.y)
    def set_tuple(self, pos: tuple[int, int]): self.x, self.y = pos

    def center_in_container_absolute(self, width: int, height: int):
        self.center_in_container_absolute_x(width)
        self.center_in_container_absolute_y(height)

    def center_in_container_absolute_x(self, width: int):
        self.x = int(width/2)

    def center_in_container_absolute_y(self, height: int):
        self.y = int(height/2)

    def get_offset_by_render_origin(self, render_origin: SpriteRenderOrigin, image: pygame.Surface) -> Transform:
        image_size_x, image_size_y = image.size
        if render_origin == SpriteRenderOrigin.TopLeft:
            return Transform(self.x, self.y)
        elif render_origin == SpriteRenderOrigin.TopRight:
            return Transform(self.x + image_size_x, self.y)
        elif render_origin == SpriteRenderOrigin.BottomLeft:
            return Transform(self.x, self.y+image_size_y)
        elif render_origin == SpriteRenderOrigin.BottomRight:
            return Transform(self.x + image_size_x, self.y + image_size_y)
        elif render_origin == SpriteRenderOrigin.Center:
            return Transform(self.x + int(image_size_x/2), self.y + int(image_size_y/2))

