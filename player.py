import pygame
from circleshape import CircleShape
from shot import Shot
from constants import*


class Player(CircleShape):
    def __init__ (self,x:int,y:int):
        super().__init__(x,y,PLAYER_RADIUS)
        self.rotation = 0
        self.cool_down = 0

    # in the player class
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def draw(self,screen):
        pygame.draw.polygon(screen,"white",self.triangle(),2)
        
    def rotate(self,dt):
        self.rotation += PLAYER_TURN_SPEED*dt
    
    def move(self, dt, direction=1):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt * direction
    
    def shoot(self):
        if self.cool_down > 0:
            return
        self.cool_down = PLAYER_SHOOT_COOLDOWN
        bullet = Shot(self.position.x,self.position.y)
        forward = pygame.Vector2(0,1).rotate(self.rotation)
        bullet.velocity += forward * PLAYER_SHOOT_SPEED
        
        
    def update(self, dt):
        keys = pygame.key.get_pressed()
        self.cool_down -= dt
        if keys[pygame.K_a]:
            self.rotate(dt)       
        if keys[pygame.K_d]:
            self.rotate(-dt)    
        if keys[pygame.K_w]:
            self.move(dt,1)    
        if keys[pygame.K_s]:
            self.move(dt,-1)
        if keys[pygame.K_SPACE]:
            self.shoot()