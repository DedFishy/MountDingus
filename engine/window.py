import pygame
from engine.scene import Scene, TransitionReason

class Window:
    """Defines a game window. This is defined as both the WM-facing stuff and the Pygame interfacing stuff."""
    def __init__(self, title: str = "Pygame", target_fps: int = 60, resolution: tuple[int, int] = (500, 500)):
        self.window = pygame.display.set_mode(resolution, pygame.RESIZABLE)

        pygame.display.set_caption(title)
        self.clock = pygame.Clock()
        self.target_fps = target_fps

        self.deltatime = 0

        self.scene = None

        self.exit = False

    def switch_to_scene(self, scene: Scene, reason: TransitionReason):
        scene.transition(reason)
        self.scene = scene

    def start(self, initial_scene: Scene):
        self.switch_to_scene(initial_scene, TransitionReason.INITIAL_SCENE)
        while not self.exit:

            if not self.scene:
                raise ValueError("Scene is null!")

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.exit = True


            self.window.fill(self.scene.BACKGROUND_COLOR)

            self.scene.update()

            pygame.display.update()
            self.deltatime = self.clock.tick(self.target_fps)/1000