import pygame
from constants import *
from player import *
pygame.init()

screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
clock = pygame.time.Clock()
dt = 0

def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
                
        screen.fill("black")
        player = Player(SCREEN_WIDTH/2,SCREEN_HEIGHT/2)
        player.draw(screen)
        
        clock.tick(60)/1000
        pygame.display.flip()

if __name__ == '__main__':
    main()
