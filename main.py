<<<<<<< HEAD
import sys

import pygame

from asteroid import Asteroid
from asteroidfield import AsteroidField
from constants import *
from player import Player
from shot import Shot
=======
import pygame

from constants import *
>>>>>>> 807f1f1 (git init)


def main():
    print("Starting Asteroids!")
    pygame.init()
<<<<<<< HEAD
    clock=pygame.time.Clock()
    dt=0

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (updatable, drawable, asteroids)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, updatable, drawable)

    print(f"Screen width: {SCREEN_WIDTH}\nScreen height: {SCREEN_HEIGHT}")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    player = Player(SCREEN_WIDTH/2 , SCREEN_HEIGHT/2)
    asteroid_field = AsteroidField()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill("black")

        updatable.update(dt)

        for dr in drawable:
            dr.draw(screen)

        for ast in asteroids:
            if ast.is_colliding(player):
                print("Game over!")
                sys.exit()

            for st in shots:
                if ast.is_colliding(st):
                    ast.split()
                    st.kill()

        pygame.display.flip()
        last_time=clock.tick(60)
        dt=last_time/1000
=======

    print(f"Screen width: {SCREEN_WIDTH}\nScreen height: {SCREEN_HEIGHT}")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    while True:
        screen.fill("black")
        pygame.display.flip()
>>>>>>> 807f1f1 (git init)


if __name__ == "__main__":
    main()
