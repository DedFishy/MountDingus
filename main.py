import pygame
from dotenv import load_dotenv
from engine.window import Window
from engine.scene import Scene

# Initialization work
pygame.init()
load_dotenv()

window = Window(Scene())
window.start()