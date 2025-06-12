import pygame #type:ignore
from population import Population

pygame.init()

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

class Obstacle:
    def __init__(self, x, y, w, h):
        self.x, self.y = x, y
        self.w, self.h = w, h
    
    def contains(self, p):
        return (self.x < p[0] < (self.x + self.w)) and (self.y < p[1] < (self.y + self.h))

class Screen:
    def __init__(self):
        self.w, self.h = 850, 650
        self.screen = pygame.display.set_mode((self.w, self.h))
        pygame.display.set_caption("Genetic Algorithm Program 3: Finding the Dot")
        self.clock = pygame.time.Clock()
        self.tiny_font = pygame.font.Font(None, 25)
        self.big_font = pygame.font.Font(None, 56)
        self.medium_font = pygame.font.Font(None, 38)
        self.pressed = False
        self.erase = False
        self.start_loc = []
        self.end_loc = []
        self.popmax = 100
        self.lifespan = 500
        self.count = 0
        self.mutation_rate = 0.01
        self.generation = 1
        self.target = (self.w/2, 150)
        self.population = Population(self.popmax, self.mutation_rate, self.w, self.h, self.target, self.lifespan)
        self.obstacles = [Obstacle(self.w/2-100, self.h/2, 200, 20)]
    
    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    self.erase = True
                elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                    self.erase = False
                elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 3:
                    self.pressed = True
                    self.start_loc = pygame.mouse.get_pos()
                elif event.type == pygame.MOUSEBUTTONUP and event.button == 3:
                    self.pressed = False
                    self.end_loc = pygame.mouse.get_pos()
                    x = min(self.start_loc[0], self.end_loc[0])
                    y = min(self.start_loc[1], self.end_loc[1])
                    w = abs(self.end_loc[0] - self.start_loc[0])
                    h = abs(self.end_loc[1] - self.start_loc[1])
                    self.obstacles.append(Obstacle(x, y, w, h))
            
            self.screen.fill(WHITE)
            self.display()
            self.show_data()

            self.count += 1
            if self.count >= self.lifespan:
                self.population.evaluate()
                self.population.selection()
                self.count = 0
                self.generation += 1

            if self.pressed: self.mouse_input()
            if self.erase: self.erase_obs()
            pygame.display.update()
            self.clock.tick(60)
    
    def display(self):
        pygame.draw.circle(self.screen, (0, 0, 0), self.target, 10)
        for i in self.obstacles:
            pygame.draw.rect(self.screen, (0, 0, 0), (i.x, i.y, i.w, i.h))
        self.population.run(self.obstacles, self.count, self.screen)
        

    def show_data(self):
        life = self.tiny_font.render(f"Lifetime: {self.count}", False, BLACK)
        lifebox = life.get_rect()
        lifebox.midleft = (50, 25)
        self.screen.blit(life, lifebox)

        gen = self.tiny_font.render(f"Generation: {self.generation}", False, BLACK)
        genbox = gen.get_rect()
        genbox.midleft = (50, 50)
        self.screen.blit(gen, genbox)

        mut = self.tiny_font.render(f"Mutation Rate: {self.population.get_mut()}", False, BLACK)
        mutbox = mut.get_rect()
        mutbox.midleft = (50, 75)
        self.screen.blit(mut, mutbox)

        acc = self.tiny_font.render(f"Avg. Accuracy: {self.population.get_acc()}%", False, BLACK)
        accbox = acc.get_rect()
        accbox.midleft = (50, 100)
        self.screen.blit(acc, accbox)
    
    def mouse_input(self):
        mouse = pygame.mouse.get_pressed()
        if mouse[2] == 1:
            mouse_pos = pygame.mouse.get_pos()
            x = min(self.start_loc[0], mouse_pos[0])
            y = min(self.start_loc[1], mouse_pos[1])
            w = abs(mouse_pos[0] - self.start_loc[0])
            h = abs(mouse_pos[1] - self.start_loc[1])
            pygame.draw.rect(self.screen, (50, 50, 50), (x, y, w, h))
    
    def erase_obs(self):
        mouse = pygame.mouse.get_pressed()
        if mouse[0] == 1:
            mouse_pos = pygame.mouse.get_pos()
            self.obstacles = [obs for obs in self.obstacles if not obs.contains(mouse_pos)]


x = Screen()
x.run()