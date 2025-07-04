import pygame
import random
from asteroid import Asteroid
from constants import *


class AsteroidField(pygame.sprite.Sprite):
    edges = [
        [
            pygame.Vector2(1, 0),
            lambda y: pygame.Vector2(-ASTEROID_MAX_RADIUS, y * SCREEN_HEIGHT),
        ],
        [
            pygame.Vector2(-1, 0),
            lambda y: pygame.Vector2(
                SCREEN_WIDTH + ASTEROID_MAX_RADIUS, y * SCREEN_HEIGHT
            ),
        ],
        [
            pygame.Vector2(0, 1),
            lambda x: pygame.Vector2(x * SCREEN_WIDTH, -ASTEROID_MAX_RADIUS),
        ],
        [
            pygame.Vector2(0, -1),
            lambda x: pygame.Vector2(
                x * SCREEN_WIDTH, SCREEN_HEIGHT + ASTEROID_MAX_RADIUS
            ),
        ],
    ]

    def __init__(self, asteroid_group):
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.spawn_timer = 0.0
        self.asteroid_group = asteroid_group

    def spawn(self, radius, position, velocity):
        asteroid = Asteroid(position.x, position.y, radius)
        asteroid.velocity = velocity


    def collision_asteroid_check( self, radius, position, asteroid):
        
        distance = position.distance_to(asteroid.position)

        if distance < radius + asteroid.radius:
            return True
        
        
                # radius, position, velocity = self.randomizer()
                # self.find_space_without_asteroid(self,radius, position)

    def find_space_without_asteroid(self,radius, position):
        story = []
        for asteroid in self.asteroid_group:
            if self.collision_asteroid_check( radius, position, asteroid):
                story.append(1)
            else:
                story.append(0)

        if 1 in story:
            radius, position, velocity = self.randomizer()
            return self.find_space_without_asteroid(radius, position)
        else:
            return radius, position

    def randomizer(self):
        edge = random.choice(self.edges)
        speed = random.randint(40, ASTEROID_MAX_MOV_SPEED)
        velocity = edge[0] * speed
        velocity = velocity.rotate(random.randint(-30, 30))
        position = edge[1](random.uniform(0, 1))
        kind = random.randint(1, ASTEROID_KINDS)
        radius = ASTEROID_MIN_RADIUS * kind

        return radius, position, velocity


    def update(self, dt):
        self.spawn_timer += dt
        if self.spawn_timer > ASTEROID_SPAWN_RATE:
            self.spawn_timer = 0

            # spawn a new asteroid at a random edge
            radius, position, velocity = self.randomizer()
            
            radius, position = self.find_space_without_asteroid(radius, position)
            
            self.spawn(radius, position, velocity)
                