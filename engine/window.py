import pygame
from engine.scene import Scene

class Window:
    """Defines a game window. This is defined as both the WM-facing stuff and the Pygame interfacing stuff."""
    def __init__(self, initial_scene: Scene, title: str = "Pygame", target_fps: int = 60, resolution: tuple[int, int] = (500, 500)):
        self.window = pygame.display.set_mode(resolution)

        self.clock = pygame.Clock()
        self.target_fps = target_fps

        self.scene = None

        self.exit = False

    def start(self):
        while not self.exit:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.exit = True

            pygame.display.update()
            self.clock.tick(self.target_fps)