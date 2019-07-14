### Flag Mania
### By Francis Tayag (Etherflux)
### Version 2
### Visit my website: etherflux.github.io

## Import all needed libraries
import pygame
from class_game import Game
from constants import *

if __name__ == "__main__":
	
	## Initialize the pygame library
	pygame.init()

	## Create a 'Game' object
	game = Game()

	## 'game_loop' method
	game.game_loop()

	## Uninitialize the pygame library
	pygame.quit()