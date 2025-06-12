from dna import DNA
from vector import Vector2D
import pygame #type:ignore

def dist(x1, y1, x2, y2):
    return ((x2 - x1)**2+(y2 - y1)**2)**0.5

class Rocket:
    def __init__(self, w, h, target, dna = None, lifespan = 400):
        self.w, self.h = w, h
        self.lifespan = lifespan
        self.target = Vector2D(target)
        self.pos = Vector2D([w/2, h-100])
        self.vel = Vector2D()
        self.acc = Vector2D()
        self.completed = False
        self.crashed = False
        if dna:
            self.dna = dna
        else:
            self.dna = DNA(lifespan=self.lifespan)
        self.fitness = 0
    
    def applyForce(self, force):
        self.acc.add(force)
    
    def stabilize(self, num, old_start, old_end, new_start, new_end):
        if old_end == 0: old_end = 1
        old_range = old_end - old_start
        new_range = new_end - new_start
        return ((num - old_start) * new_range / old_range) + new_start
    
    def calculateFitness(self):
        d = dist(self.pos.x(), self.pos.y(), self.target.x(), self.target.y())
        self.fitness = self.stabilize(d, 0, self.w, self.w, 0)
        if self.completed:
            self.fitness *= 10
            return 0
        if self.crashed: self.fitness *= 0.1
        return 1
    
    def update(self, obstacles, count):
        d = dist(self.pos.x(), self.pos.y(), self.target.x(), self.target.y())
        if d <= 10:
            self.completed = True
            self.pos = Vector2D(self.target.get())

        for i in obstacles:
            if i.contains(self.pos.get()):
                self.crashed = True
        if not (0 < self.pos.x() < self.w):
            self.crashed = True
        if not (0 < self.pos.y() < self.h):
            self.crashed = True
        
        self.applyForce(self.dna.genes[count])
        if not self.completed and not self.crashed:
            self.vel.add(self.acc)
            self.pos.add(self.vel)
            self.acc.mul(0)
            self.vel.limit(4)
    
    def show(self, screen):
        rect_surf = pygame.Surface((5, 25), pygame.SRCALPHA)
        pygame.draw.rect(rect_surf, (0, 0, 0, 128), (0, 0, 5, 25))
        angle = self.vel.heading()
        rotated_surf = pygame.transform.rotate(rect_surf, angle)
        rotated_rect = rotated_surf.get_rect(center=self.pos.get())
        screen.blit(rotated_surf, rotated_rect.topleft)
    
    def get(self): return self.pos.get()