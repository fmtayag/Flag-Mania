## Import needed libraries
from constants import *
import pygame
import os

## Image class
class Image():

    ## Initialize method
    def __init__(self, filename, position):

        ## Variables from parameter
        self.filename = filename
        self.position = position

        ## Sets the path
        self.path = os.path.join("Resources", "Images", self.filename + ".png")

        ## Loads iamge
        self.image = pygame.image.load(self.path)
        self.image_rect = self.image.get_rect()
        self.image_rect.x = self.position[0]
        self.image_rect.y =  self.position[1]

    ## Render method
    def render(self):

        return self.image

    ## Resize method
    def resize(self, size):

        self.image = pygame.transform.scale(self.image, size)