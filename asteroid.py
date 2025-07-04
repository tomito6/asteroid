from circleshape import CircleShape
import pygame
from constants import *
import random
import math

class Asteroid(CircleShape):
   def __init__(self, x, y, radius):
      super().__init__(x, y, radius)
      # self.mass = 4/3 * math.pi * radius**3
      self.mass = 1


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


         dy2 = 1.5*new_radius * math.cos(math.radians(-angle))
         dx2 = 1.5*new_radius * math.sin(math.radians(-angle))
         asteroid2 = Asteroid(x+dx2, y+dy2, new_radius)
         asteroid2.velocity = velocity.rotate(-angle) * 1.2

         self.kill()

       
   def collision_asteroid_check(self, asteroid):
        
      distance = self.position.distance_to(asteroid.position)

      if distance < self.radius + asteroid.radius:
         return True

   def collision_asteroid(self, asteroid):
      
      n = (asteroid.position - self.position).normalize()
      

      v1n = self.velocity.dot(n) 

      v2n = asteroid.velocity.dot(n)

      v1_n =   (v1n*(self.mass - asteroid.mass) + 2*asteroid.mass*v2n)/(self.mass + asteroid.mass)

      v2_n =   (v2n*(-self.mass + asteroid.mass) + 2*self.mass*v1n)/(self.mass + asteroid.mass)

      t = pygame.Vector2(-n.y, n.x)

      v1t = self.velocity.dot(t)
      v2t = asteroid.velocity.dot(t)


      self.velocity = v1_n * n + v1t * t
      asteroid.velocity = v2_n * n + v2t * t