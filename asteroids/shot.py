from circleshape import CircleShape
from constants import *
import pygame

class Shot(CircleShape):
    containers = ()

    def __init__(self, x, y, direction):
        super().__init__(x, y, SHOT_RADIUS)
        self.velocity = direction * PLAYER_SHOOT_SPEED

    def update(self, dt):
        self.position += self.velocity * dt

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius)
    


