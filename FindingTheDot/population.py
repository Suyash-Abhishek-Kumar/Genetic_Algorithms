from rocket import Rocket
from random import random

class Population:
    def __init__(self, size, mutation_rate, w, h, target, lifespan):
        self.w, self.h = w, h
        self.lifespan = lifespan
        self.target = target
        self.popmax = size
        self.mutation_rate = mutation_rate
        self.rockets = [Rocket(w, h, target, lifespan=self.lifespan) for _ in range(self.popmax)]
        self.totfit = 0
        self.maxfit = 0
        self.failcount = 0
        self.passed = False
    
    def evaluate(self):
        self.totfit = 0
        self.maxfit = 0
        for i in self.rockets:
            x = i.calculateFitness()
            self.totfit += i.fitness
            if x == 0: self.passed = True
        
        if self.passed:
            self.failcount = 0
            self.mutation_rate = 0.01
        else:
            self.failcount += 1
        self.passed = False
        
        for i in self.rockets:
            i.fitness /= self.totfit
            if self.maxfit < i.fitness:
                self.maxfit = i.fitness
    
    def acc_rej(self):
        total = 0
        choice = random()
        for i in self.rockets:
            total += i.fitness
            if total > choice:
                return i

    def selection(self):
        newRockets = []
        if self.failcount > 9 and self.maxfit < 0.5 and self.failcount%3==0:
            self.mutation_rate = min(0.16, round(self.mutation_rate + 0.05, 4))
        elif self.failcount > 9 and self.maxfit >= 0.6:
            self.mutation_rate = max(0.01, round(self.mutation_rate - 0.05, 4))


        for i in range(self.popmax):
            parentA = self.acc_rej()
            parentB = self.acc_rej()
            # while parentB == parentA:
            #     parentB = self.acc_rej()
            child = parentA.dna.crossover(parentB.dna)
            child.mutate(self.mutation_rate)
            newRockets.append(Rocket(self.w, self.h, self.target, dna=child, lifespan=self.lifespan))
        self.rockets = newRockets
    
    def run(self, obstacles, count, screen):
        for i in self.rockets:
            i.update(obstacles, count)
            i.show(screen)

    def get_mut(self): return self.mutation_rate
    def get_acc(self): return round((self.totfit/self.popmax)/85, 3)
