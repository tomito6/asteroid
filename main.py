import pygame
from constants import *
def main():

   print("Starting Asteroids!")
   print(f"Screen width: {SCREEN_WIDTH}")
   print(f"Screen height: {SCREEN_HEIGHT}")

   
   
   pygame.init()
   state = pygame.get_init()

   while state:
      for event in pygame.event.get():
         if event.type == pygame.QUIT:
            state = False
            return
   
            


      screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

      a = pygame.Surface.fill(screen, color="black")
      
      pygame.display.flip()

   




if __name__ == "__main__":
    main()