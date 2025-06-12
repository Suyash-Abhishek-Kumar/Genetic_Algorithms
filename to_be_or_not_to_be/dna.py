from random import choice, randint, random
possible_genes = [chr(i) for i in range(65, 123)]
possible_genes.extend([chr(32), chr(46), chr(63)])

class DNA:
    def __init__(self, length):
        self.length = length
        self.fitness = 0
        self.genes = [choice(possible_genes) for _ in range(self.length)]
        self.phenotype = None
    
    def get_phrase(self):
        self.phenotype = "".join(self.genes)
        return self.phenotype
    
    def calc_Fitness(self, target):
        self.fitness = 0
        for i in range(self.length):
            if self.genes[i] == target[i]:
                self.fitness += 1
        self.fitness /= self.length    # Normalizing the fitness between 0 and 1
    
    def crossover(self, partner):
        child = DNA(self.length)
        midpt = randint(0, self.length - 1)
        for i in range(self.length):
            if i < midpt:
                child.genes[i] = self.genes[i]
            else:
                child.genes[i] = partner.genes[i]
        return child

    def mutation(self, mutation_rate):
        for i in range(self.length):
            if random() < mutation_rate:
                self.genes[i] = choice(possible_genes)