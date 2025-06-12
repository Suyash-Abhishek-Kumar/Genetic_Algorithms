from random import randint, random
from vector import randomV

class DNA:
    def __init__(self, lifespan = 400, maxForce = 0.2, genes = None):
        self.lifespan = lifespan
        self.maxForce = maxForce
        if genes:
            self.genes = genes
        else:
            self.genes = [randomV() for _ in range(self.lifespan)]
            for i in self.genes:
                i.setMag(self.maxForce)
    
    def crossover(self, partner):
        child = []
        midpt = randint(0, self.lifespan - 1)
        for i in range(self.lifespan):
            if i < midpt:
                child.append(self.genes[i])
            else:
                child.append(partner.genes[i])
        return DNA(genes = child, lifespan=self.lifespan)
    
    def mutate(self, mutation_rate):
        for i in range(self.lifespan):
            if random() < mutation_rate:
                self.genes[i] = randomV()
                self.genes[i].setMag(self.maxForce)