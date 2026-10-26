import pygame
from constants import SCREEN_HEIGHT, SCREEN_WIDTH
from logger import log_state, log_event
from player import Player
from asteroidfield import AsteroidField
from asteroid import Asteroid
from circleshape import CircleShape
from shot import Shot
import sys


def main():
    pygame.init()
    frame_clock = pygame.time.Clock()
    dt = 0.0
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    print(f"Starting Asteroids with pygame version {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, updatable, drawable)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    ast_field = AsteroidField()
    while True:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        updatable.update(dt)
        for ast in asteroids:
            if ast.collides_with(player):
                log_event("player_hit")
                print("Game over!")
                sys.exit()
        for ast in asteroids:
            for pew in shots:
                if ast.collides_with(pew):
                    log_event("asteroid_shot")
                    ast.split()
                    pew.kill()
        for obj in drawable:
            obj.draw(screen)
        pygame.display.flip()
        dt = frame_clock.tick(60) / 1000




if __name__ == "__main__":
    main()
