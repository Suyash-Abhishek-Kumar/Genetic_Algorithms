from dna import DNA
from math import floor
from random import randint

class Population:
    def __init__(self, target, mutation_rate, size):
        self.target = list(target)
        self.mutationRate = mutation_rate
        self.popmax = size
        self.generations = 0
        self.best = ""
        self.finished = False
        self.population = [DNA(len(self.target)) for _ in range(self.popmax)]
        self.matingPool = []
    
    def calcFitness(self):
        for i in self.population:
            i.calc_Fitness(self.target)
    
    def stabilize(self, num, old_start, old_end, new_start, new_end):
        if old_end == 0: old_end = 1
        old_range = old_end - old_start
        new_range = new_end - new_start
        return ((num - old_start) * new_range / old_range) + new_start
    
    def natural_selection(self):
        self.matingPool = []
        maxFitness = 0

        for i in self.population:
            if i.fitness > maxFitness:
                maxFitness = i.fitness
        
        for i in self.population:
            fitness = self.stabilize(i.fitness, 0, maxFitness, 0, 1)
            n = floor(fitness * 100)
            for _ in range(n):
                self.matingPool.append(i)
        
    
    def new_gen(self):
        for i in range(self.popmax):
            a = randint(0, len(self.matingPool) - 1)
            b = randint(0, len(self.matingPool) - 1)
            parentA = self.matingPool[a]
            parentB = self.matingPool[b]
            child = parentA.crossover(parentB)
            child.mutation(self.mutationRate)
            self.population[i] = child
        self.generations += 1

    def evaluate(self):
        best = 0
        phrase = ""
        for i in self.population:
            if i.fitness > best:
                best = i.fitness
                phrase = i.get_phrase()
        self.best = phrase
        if best == 1: self.finished = True
    
    def getAverageFitness(self):
        avg = 0
        for i in self.population:
            avg += i.fitness
        avg /= self.popmax
        return avg
    
    def getBest(self):
        return self.best
    
    def isFinished(self):
        return self.finished
    
    def getGenerations(self):
        return self.generations