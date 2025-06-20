import pygame #type:ignore
from Vehicle import Vehicle

pygame.init()

class Screen:
    def __init__(self):
        self.w, self.h = 850, 650
        self.screen = pygame.display.set_mode((self.w, self.h))
        pygame.display.set_caption("Genetic Algorithm Program 3: Finding the Dot")
        self.clock = pygame.time.Clock()
        self.tiny_font = pygame.font.Font(None, 25)
        self.big_font = pygame.font.Font(None, 56)
        self.medium_font = pygame.font.Font(None, 38)
        self.target = None

    def run(self):
        running = True
        vehicles = [Vehicle(self.w, self.h) for i in range(10)]
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            
            self.screen.fill((0, 0, 0))
            self.show_target()
            for i in vehicles:
                i.update()
                i.seek(self.target)
                i.show(self.screen)

            pygame.display.update()
            self.clock.tick(60)
    
    def show_target(self):
        mouse = pygame.mouse.get_pos()
        self.target = mouse
        pygame.draw.circle(self.screen, (255, 255, 255), mouse, 10)

x = Screen()
x.run()