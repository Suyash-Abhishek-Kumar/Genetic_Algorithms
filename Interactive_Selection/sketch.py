import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pygame #type:ignore
from population import Population
from UI.buttons import Button

pygame.init()

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

class Screen:
    def __init__(self):
        self.w, self.h = 800, 450
        self.screen = pygame.display.set_mode((self.w, self.h))
        pygame.display.set_caption("Genetic Algorithm Program 2: Evolving Flowers")
        self.clock = pygame.time.Clock()
        self.tiny_font = pygame.font.Font(None, 25)
        self.big_font = pygame.font.Font(None, 48)
        self.medium_font = pygame.font.Font(None, 38)
        self.mutation_rate = 0.05
        self.popmax = 8
        self.population = Population(self.mutation_rate, self.popmax)
        self.button = Button(self.screen, (400, 350), 3, "Next Generation", self.nextGen, BLACK, fixed_size=(180, 40), button_color=(205, 205, 205))
    
    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        if self.button.collision_check():
                            self.button.function()
            
            self.screen.fill(WHITE)
            self.draw()
            self.button.run()
            pygame.display.update()
            self.clock.tick(60)
        
    def nextGen(self):
        self.population.selection()
        self.population.reproduction()

    def draw(self):
        heading = self.big_font.render("Flower Evolution: Interactive Selection", False, BLACK)
        headbox = heading.get_rect()
        headbox.midtop = (400, 50)
        self.screen.blit(heading, headbox)

        gen = self.tiny_font.render("Number of Generations: {}".format(self.population.generations), False, BLACK)
        genbox = gen.get_rect()
        genbox.midtop = (400, 400)
        self.screen.blit(gen, genbox)
        
        self.population.display(self.screen)
        mouseX, mouseY = pygame.mouse.get_pos()
        self.population.rollover(mouseX, mouseY)


x = Screen()
x.run()