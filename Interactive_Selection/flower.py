from math import floor, sin, cos, pi
from dna import DNA
import pygame #type:ignore

class Rectangle:
    def __init__(self, x, y, w, h):
        self.x, self.y = x, y
        self.w, self.h = w, h
    
    def contains(self, px, py):
        return (self.x < px < (self.x + self.w)) and (self.y < py < (self.y + self.h))

class Flower:
    def __init__(self, dna: DNA, x, y):
        self.isTouching = False
        self.dna = dna
        self.x, self.y = x, y
        self.w, self.h = 70, 140
        self.fitness = 1
        self.boundingBox = Rectangle(self.x, self.y, self.w, self.h)
        self.font = pygame.font.Font(None, 25)
    
    def stabilize(self, num, old_start, old_end, new_start, new_end):
        if old_end == 0: old_end = 1
        old_range = old_end - old_start
        new_range = new_end - new_start
        return ((num - old_start) * new_range / old_range) + new_start


    def display(self, screen):
        genes = self.dna.genes
        c = (genes[0], genes[1], genes[2]) # petal color
        c = tuple(map(lambda val: self.stabilize(val, 0, 1, 0, 255), c))
        size = self.stabilize(genes[3], 0, 1, 4, 16)  # petal size
        count = floor(self.stabilize(genes[4], 0, 1, 2, 16))  # petal count
        centerColor = (genes[5], genes[6], genes[7])  # center color
        centerColor = tuple(map(lambda val: self.stabilize(val, 0, 1, 0, 255), centerColor))
        centerSize = self.stabilize(genes[8], 0, 1, 0, 12)  # center size
        stemColor = (genes[9], genes[10], genes[11])  # stem color
        stemColor = tuple(map(lambda val: self.stabilize(val, 0, 1, 0, 255), stemColor))
        stemLength = self.stabilize(genes[12], 0, 1, 50, 100)  # stem length

        # Bounding Box
        if self.isTouching:
            pygame.draw.rect(screen, (205, 205, 205), (self.x, self.y, self.w, self.h))
        pygame.draw.rect(screen, (0, 0, 0), (self.x, self.y, self.w, self.h), 2)
        
        # Stem
        pygame.draw.line(screen, stemColor, (self.x + self.w/2, self.y + self.h - stemLength), (self.x + self.w/2, self.y + self.h - 3), 5)

        # Petals
        for i in range(count):
            angle = self.stabilize(i, 0, count, 0, 2*pi)
            x = size * cos(angle) + self.x + self.w/2
            y = size * sin(angle) + self.y + self.h - stemLength
            pygame.draw.circle(screen, c, (x, y), size)
            sorted_c = tuple(sorted([c[0], c[1], c[2]]))
            pygame.draw.circle(screen, sorted_c, (x, y), size*0.7)
        
        # Center
        pygame.draw.circle(screen, centerColor, (self.x + self.w/2, self.y + self.h - stemLength), centerSize)

        # Fitness
        fitness = self.font.render("{}".format(floor(self.fitness)), False, (0, 0, 0))
        fitbox = fitness.get_rect()
        fitbox.midtop = (self.x + self.w / 2, self.y + self.h + 15)
        screen.blit(fitness, fitbox)



    def rollover(self, mx, my):
        if self.boundingBox.contains(mx, my):
            self.isTouching = True
            self.fitness += 0.25
        else:
            self.isTouching = False
    