import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from shot import Shot
from asteroidfield import AsteroidField

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    the_asteroids = pygame.sprite.Group()
    bullets = pygame.sprite.Group()
    
    Player.containers = (updatable,drawable)
    player = Player(SCREEN_WIDTH/2,SCREEN_HEIGHT/2)
    
    Asteroid.containers = (the_asteroids,updatable,drawable)
    AsteroidField.containers = (updatable)
    asteroidfield = AsteroidField()
    Shot.containers = bullets , updatable,drawable
    
    
    
    dt = 0
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        updatable.update(dt)
        #checking to see if the asteroids are hitting the player
        for obj in the_asteroids:
            if obj.check_collisions(player):
                print("Game over!")
                exit()
            #checking to see if the bullets hit the asteriod    
            for shot in bullets:
                if obj.check_collisions(shot):
                    obj.split()
                    shot.kill()
        screen.fill("black")
        
        for d in drawable:
            d.draw(screen)
        
        pygame.display.flip()
        dt = clock.tick(60)/1000

if __name__ == '__main__':
    main()
