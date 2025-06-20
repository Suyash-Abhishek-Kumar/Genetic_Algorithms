from vector import Vector2D, stabilize, randomV
from random import randint
import pygame #type:ignore

class Vehicle:
    def __init__(self, w, h):
        self.pos = Vector2D([randint(w/2-20, w/2+20), randint(h/2-20, h/2+20)])
        self.vel = Vector2D()
        self.acc = Vector2D()
        self.maxForce = 0.3
        self.size = randint(5, 15)
        self.maxSpeed = stabilize(self.size, 5, 15, 5, 50)
    
    def applyForce(self, force):
        self.acc.add(force)
    
    def update(self):
        self.vel.add(self.acc)
        self.vel.limit(self.maxSpeed)
        self.pos.add(self.vel)
        self.acc.mul(0)
    
    def eat(self, targets):
        record = 99999
        closest = -1
        for i in range(len(targets)):
            if self.pos.dist(targets[i]) < record:
                closest = i
                record = self.pos.dist(targets[i])
        self.seek(closest)
    
    def seek(self, target):
        desired = Vector2D(list(target))
        desired.sub(self.pos)
        desired.setMag(self.maxSpeed)
        steer = Vector2D(desired.get())
        steer.sub(self.vel)
        steer.limit(self.maxForce)
        self.applyForce(steer)
    
    def show(self, screen):
        rect_surf = pygame.Surface((15, 25), pygame.SRCALPHA)
        triangle_points = [(7.5, 25), (0, 0), (15, 0)]
        pygame.draw.polygon(rect_surf, (255, 255, 255, 128), triangle_points)
        angle = self.vel.heading()
        rotated_surf = pygame.transform.rotate(rect_surf, angle)
        rotated_rect = rotated_surf.get_rect(center=self.pos.get())
        screen.blit(rotated_surf, rotated_rect.topleft)