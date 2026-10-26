from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS, LINE_WIDTH
from logger import log_event
import pygame
import random

class Asteroid(CircleShape):
    def __init__(self, x: float, y: float, radius: float) -> None:
        super().__init__(x, y, radius)

    def draw(self, screen: pygame.Surface) -> None:
        pygame.draw.circle(screen, "white", self.position,self.radius, LINE_WIDTH)

    def update(self, dt: float) -> None:
        self.position += self.velocity * dt

    def split(self) -> None:
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        log_event("asteroid_split")
        new_angle = random.uniform(20, 50)
        ast1_vector = self.velocity.rotate(new_angle)
        ast2_vector = self.velocity.rotate(1 - new_angle)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        ast1 = Asteroid(self.position.x, self.position.y, new_radius)
        ast1.velocity = ast1_vector * 1.2
        ast2 = Asteroid(self.position.x, self.position.y, new_radius)
        ast2.velocity = ast2_vector * 1.2
