import pygame, random
from constants import *
from circleshape import CircleShape

class Asteroid(CircleShape):
    def __init__ (self,x:int,y:int,radius:float):
        super().__init__(x,y,radius)
        
    def draw(self,screen):
        pygame.draw.circle(screen,'green',self.position,self.radius,2)
    
    def update(self,dt):
        self.position += self.velocity * dt
        
    def split(self):
        self.kill()
        #checking size of asteriod
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        
        #making new angle if asteriods not killed
        random_angle = random.uniform(20.0,50.0)
        
        #making new velocity for smaller asteriods when broken down
        new_velocity1 = self.velocity.rotate(random_angle)
        new_velocity2 = self.velocity.rotate(-random_angle)
        
        #make a new radius for asteriod when shot
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        
        #create new asteriod for group
        new_asteroid1 = Asteroid(self.position.x,self.position.y,new_radius)
        new_asteroid2 = Asteroid(self.position.x,self.position.y,new_radius)
        
        #add new velocity to asteriods
        new_asteroid1.velocity = new_velocity1 * 1.2
        new_asteroid2.velocity = new_velocity2 * 1.2