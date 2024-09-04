import pygame
from dotenv import load_dotenv
from engine.window import Window
from engine.scene import Scene
from scenes.mainmenu import MainMenu

# Initialization work
pygame.init()
load_dotenv()

window = Window("Mount Dingus")
window.start(MainMenu(window))