import pygame
from constants import *
from player import Player
from asteroidfield import AsteroidField
from asteroid import Asteroid
from shot import Shot

def main():


   print("Starting Asteroids!")
   print(f"Screen width: {SCREEN_WIDTH}")
   print(f"Screen height: {SCREEN_HEIGHT}")

   
   
   pygame.init()

   time = pygame.time.Clock()
   dt = 0
   screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
   updatable = pygame.sprite.Group()
   drawable = pygame.sprite.Group()
   asteroids = pygame.sprite.Group()
   shots = pygame.sprite.Group()

   Asteroid.containers = (asteroids, updatable, drawable)
   Player.containers = (updatable, drawable)
   AsteroidField.containers = (updatable)
   Shot.containers = (shots, updatable, drawable)

   asteroidfield = AsteroidField(asteroids)  
   player = Player(x = SCREEN_WIDTH/2 , y = SCREEN_HEIGHT/2, radius = PLAYER_RADIUS)
   while True:
      for event in pygame.event.get():
         if event.type == pygame.QUIT:
            pygame.quit()
            return

      for circ in asteroids:
         if circ.collision_check(player):
            print("Game over!")
            pygame.quit()
            return
         
      for circ in asteroids:
         for sh in shots:
            if sh.collision_check(circ):
               sh.kill()
               circ.split()      

      asteroid_list = list(asteroids)

      for i, ast1 in enumerate(asteroid_list):
         for ast2 in asteroid_list[i+1:]:
            if ast1 != ast2 and ast1.collision_asteroid_check(ast2):
               ast1.collision_asteroid(ast2)
               

      updatable.update(dt)
      
      screen.fill("black")
      for obj in drawable:

         obj.draw(screen)
      pygame.display.flip()
      

      dt = time.tick(60) / 1000




if __name__ == "__main__":
    main()