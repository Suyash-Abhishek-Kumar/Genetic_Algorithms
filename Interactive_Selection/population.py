from random import random
from dna import DNA
from flower import Flower

class Population:
    def __init__(self, mutation_rate, size):
        self.mutation_rate = mutation_rate
        self.popmax = size
        self.generations = 0
        self.image = [Flower(DNA(), 45+i*90, 120) for i in range(self.popmax)]

    def display(self, screen):
        for i in range(self.popmax):
            self.image[i].display(screen)
    
    def rollover(self, mx, my):
        for i in range(self.popmax):
            self.image[i].rollover(mx, my)
        
    def weighted_selection(self):
        index = 0
        start = random()
        while start > 0:
            start -= self.image[index].fitness
            index += 1
        index -= 1
        return self.image[index]
    
    def selection(self):
        totalFitness = 0
        for i in range(self.popmax):
            totalFitness += self.image[i].fitness
        
        for i in range(self.popmax):
            self.image[i].fitness /= totalFitness
    
    def reproduction(self):
        newGen = []
        for i in range(self.popmax):
            parentA = self.weighted_selection()
            parentB = self.weighted_selection()
            child_dna = parentA.dna.crossover(parentB.dna)  # Use DNA instances from parents
            child_dna.mutate(self.mutation_rate)
            newGen.append(Flower(child_dna, 45+i*90, 120))
        self.image = newGen
        self.generations += 1