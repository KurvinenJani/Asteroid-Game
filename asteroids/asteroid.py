import pygame
import random
from circleshape import CircleShape
from constants import *

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

        
        # Luo läpinäkyvä pinta asteroidille
        self.image = pygame.Surface((radius * 2, radius * 2), pygame.SRCALPHA)
        pygame.draw.circle(self.image, "white", (radius, radius), radius, 2)

        # Luo törmäysalue rect, jonka keskipiste on asteroidin paikassa
        self.rect = self.image.get_rect(center=self.position)

    def update(self, dt):
        self.position += self.velocity * dt
        self.rect.center = self.position  # Päivitä rectin sijainti

    def draw(self, screen):
        screen.blit(self.image, self.rect)  # Piirrä kuva ruudulle
    
    def split(self):
        self.kill()

        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        
        new_radius = self.radius - ASTEROID_MIN_RADIUS

        random_angle = random.uniform(20, 50)

        direction1 = self.velocity.rotate(random_angle) * 1.2
        direction2 = self.velocity.rotate(-random_angle) * 1.2

        from asteroid import Asteroid

        a1 = Asteroid(self.position.x, self.position.y, new_radius)
        a2 = Asteroid(self.position.x, self.position.y, new_radius)

        a1.velocity = direction1
        a2.velocity = direction2

        if hasattr(self, "groups"):
            for group in self.groups():
                group.add(a1)
                group.add(a2) 
