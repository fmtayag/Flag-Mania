## Import needed libraries
from constants import *
import pygame
import os

## The 'Label' class, for texts
class Label:

    ## 'Constructor' method
    def __init__(self, text, filename, size, color, position):

        ## Variables from parameter
        self.text = text
        self.filename = filename
        self.size = size
        self.color = color
        self.position = position ## Is a list [x_position, y_position]

        ## Sets the path
        self.path = os.path.join("Resources", "Fonts", self.filename + ".ttf")

        ## Create 'Font' object
        self.font = pygame.font.Font(self.path, self.size)

        ## Renders the label
        self.rendered = self.font.render(self.text, True, self.color)
        self.rendered_rect = self.rendered.get_rect()
        self.rendered_rect.x = self.position[0]
        self.rendered_rect.y = self.position[1]

    ## Render method
    def render(self):

        self.rendered = self.font.render(self.text, True, self.color)
        return self.rendered

    ## Special effect, 'depresses' or grays out the label
    def depress(self, mouse_position):

        ## Checks if the object's rect attribute collides with the mouse position
        if self.rendered_rect.collidepoint(mouse_position):

            self.color = GRAY
            self.render()

        else:

            self.color = WHITE
            self.render()

    ## Special effect, makes the label go down
    def go_down(self):

        self.position[1] += 5

    def change_text(self, text):

        self.text = text