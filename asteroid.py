from circleshape import CircleShape
import pygame
from constants import *
import random

class Asteroid(CircleShape):
   def __init__(self, x, y, radius):
      super().__init__(x, y, radius)


   def draw(self, screen):
      pygame.draw.circle(screen, "white", center = self.position, radius = self.radius, width = 2)


   def update(self, dt):
      self.position += self.velocity *dt

   def split(self):
      old_radius = self.radius
      x = self.position.x
      y = self.position.y
      velocity = self.velocity
      if old_radius <= ASTEROID_MIN_RADIUS:
         self.kill()
         return
      
      else:
         angle = random.uniform(20,50)
         old_radius = self.radius
         asteroid1 = Asteroid(x, y, old_radius - ASTEROID_MIN_RADIUS)
         asteroid1.velocity = velocity.rotate(angle) * 1.2

         asteroid2 = Asteroid(x, y, old_radius - ASTEROID_MIN_RADIUS)
         asteroid2.velocity = velocity.rotate(-angle) * 1.2

         self.kill()

    