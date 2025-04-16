import pygame
from constants import *
from player import *
from asteroid import *
from asteroidfield import *
from shot import *
import sys

def main():
    pygame.init()

    screen = pygame.display.set_mode(size=(SCREEN_WIDTH, SCREEN_HEIGHT))
    
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    clock = pygame.time.Clock()
    dt = 0

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    Shot.containers = (shots, updatable, drawable)
    AsteroidField.containers = updatable

    player = Player((SCREEN_WIDTH / 2),(SCREEN_HEIGHT/2))
    asteroid_field = AsteroidField()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        dt = clock.tick(60)/1000
        
        updatable.update(dt)

        for asteroid in asteroids:
            if player.is_touching(asteroid):
                print("Game Over!")
                screen.fill((255, 0, 0)) #flash red
                pygame.display.flip()
                pygame.time.delay(600)  # 600ms delay
                sys.exit()
      
            for shot in shots:
                if asteroid.is_touching(shot):
                    shot.kill()
                    asteroid.split()

        screen.fill((0,0,0))
        
        for obj in drawable:
            obj.draw(screen)
            
        pygame.display.flip()

if __name__ == "__main__":
    main()
