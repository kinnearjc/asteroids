# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from player import *
from asteroid import *
from asteroidfield import *
import sys

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()


    AsteroidField.containers = (updatable,)
    Asteroid.containers = (asteroids, updatable, drawable)
    Player.containers =(updatable, drawable)
    Shot.containers = (updatable, drawable, shots)


    my_clock= pygame.time.Clock()
    dt = 0
    p1 = Player((SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2))
    a1 = AsteroidField()

    done = False
    while done == False:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        updatable.update(dt)
        screen.fill((0, 0, 0))

        for drawable_obj in drawable:
            drawable_obj.draw(screen)

        for asteroid in asteroids:

            if (p1.check_collision(asteroid)):
                print("GAME OVER")
                sys.exit()
            
            for bullet in shots:
                    if(bullet.check_collision(asteroid)):
                        asteroid.split()
                

        pygame.display.flip()
        dt = my_clock.tick(60)/ 1000





if __name__ == "__main__":
    main()