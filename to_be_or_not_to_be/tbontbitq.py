from population import Population
from math import ceil
import pygame #type:ignore

pygame.init()

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

class Screen:
    def __init__(self):
        self.w, self.h = 950, 650
        self.screen = pygame.display.set_mode((self.w, self.h))
        pygame.display.set_caption("Genetic Algorithm Program 1: Evolving Phrases")
        self.clock = pygame.time.Clock()
        self.tiny_font = pygame.font.Font(None, 25)
        self.big_font = pygame.font.Font(None, 56)
        self.medium_font = pygame.font.Font(None, 38)
        self.target = "To be or not to be"
        self.popmax = 100
        self.mutation_rate = 0.01
        self.genBests = []
        self.population = Population(self.target, self.mutation_rate, self.popmax)
        self.population.calcFitness()
    
    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            if not self.population.isFinished():
                self.population.natural_selection()
                self.population.new_gen()
                self.population.calcFitness()
                self.population.evaluate()
                self.genBests.append(self.population.getBest())

            self.screen.fill(WHITE)
            self.show_data()

            pygame.display.update()
            self.clock.tick(60)
    
    def show_data(self):
        answer = self.population.getBest()
        stats = [self.population.getGenerations(), round(self.population.getAverageFitness(), 4)*100, self.popmax, self.mutation_rate * 100]

        heading = self.big_font.render("Best Phrase:", False, BLACK)
        phrase = self.big_font.render(answer, False, BLACK)
        gens = self.medium_font.render("No. of generations: {}".format(stats[0]), False, BLACK)
        avg_fit = self.medium_font.render("Average Fitness: {}%".format(stats[1]), False, BLACK)
        totPop = self.medium_font.render("Total Population: {}".format(stats[2]), False, BLACK)
        mutn_rate = self.medium_font.render("Mutation Rate: {}%".format(stats[3]), False, BLACK)
        best_heading = self.medium_font.render("Best Of Each Generation:", False, BLACK)

        headbox = heading.get_rect()
        phbox = phrase.get_rect()
        genbox = gens.get_rect()
        avgbox = avg_fit.get_rect()
        tpbox = totPop.get_rect()
        mrbox = mutn_rate.get_rect()
        bhbox = best_heading.get_rect()
        
        headbox.midleft = (30, 150)
        phbox.midleft = (30, 210)
        genbox.midleft = (30, 300)
        avgbox.midleft = (30, 350)
        tpbox.midleft = (30, 400)
        mrbox.midleft = (30, 450)
        bhbox.midleft = (550, 50)
        
        self.screen.blit(heading, headbox)
        self.screen.blit(phrase, phbox)
        self.screen.blit(gens, genbox)
        self.screen.blit(avg_fit, avgbox)
        self.screen.blit(totPop, tpbox)
        self.screen.blit(mutn_rate, mrbox)
        self.screen.blit(best_heading, bhbox)

        self.print_bests()
    
    def print_bests(self):
        maxi = 20
        rev = self.genBests[::-1]
        step = ceil(len(rev) / maxi)
        count = 0

        for i in range(0, min(len(rev), maxi * step), step):
            gen_num = len(rev) - i
            text = self.tiny_font.render(f"Generation {gen_num}: {rev[i]}", False, BLACK)
            textbox = text.get_rect()
            textbox.midleft = (550, 100 + 25 * count)
            self.screen.blit(text, textbox)
            count += 1


x = Screen()
x.run()