from random import random, randint

class DNA:
    def __init__(self):
        self.gene_length = 13
        self.genes = [random() for _ in range(self.gene_length)]
    
    def crossover(self, partner):
        child = DNA()
        midpt = randint(0, self.gene_length - 1)
        for i in range(self.gene_length):
            if i < midpt:
                child.genes[i] = self.genes[i]
            else:
                child.genes[i] = partner.genes[i]
        return child

    def mutate(self, mutation_rate):
        for i in range(self.gene_length):
            if random() < mutation_rate:
                self.genes[i] = random()