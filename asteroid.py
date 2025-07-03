from circleshape import CircleShape
import pygame
from constants import *
import random
import math

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
         old = self.radius
         math.cos(math.radians(angle))
         new_radius = self.radius - ASTEROID_MIN_RADIUS
         dx1 = 1.5*new_radius * math.cos(math.radians(angle))
         dy1 = 1.5*new_radius * math.sin(math.radians(angle))
         asteroid1 = Asteroid(x+dx1, y+dy1, new_radius)
         asteroid1.velocity = velocity.rotate(angle) * 1.2


         dy2 = 1.5*new_radius * math.cos(math.radians(angle))
         dx2 = 1.5*new_radius * math.sin(math.radians(angle))
         asteroid2 = Asteroid(x+dx2, y+dy2, new_radius)
         asteroid2.velocity = velocity.rotate(-angle) * 1.2

         self.kill()

       
   def collision_asteroid_check(self, asteroid):
        
      distance = self.position.distance_to(asteroid.position)

      if distance < self.radius + asteroid.radius:
         return True

   def collision_asteroid(self, asteroid):
      self.velocity =  -self.velocity
      asteroid.velocity = -asteroid.velocity  
        
    