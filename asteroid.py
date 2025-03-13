import pygame
from circleshape import CircleShape

class Asteroid(CircleShape):
    def __init__ (self,x:int,y:int,radius:float):
        super().__init__(x,y,radius)
        
    def draw(self,screen):
        pygame.draw.circle(screen,'green',(self.position.x,self.position.y),self.radius,2)
    
    def update(self,dt):
        self.position += self.velocity * dt
        