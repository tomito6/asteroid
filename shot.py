from circleshape import CircleShape
import pygame
from constants import *

class Shot(CircleShape):

   def __init__(self, x, y, radius = SHOT_RADIUS):
      super().__init__(x, y, radius)
      self.radius = SHOT_RADIUS

   def draw(self, screen):
      pygame.draw.circle(screen, "white", center = self.position, radius = self.radius, width = 1)


   def update(self,dt):
      self.position = self.position + self.velocity 
