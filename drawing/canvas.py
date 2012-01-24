import pygame

class Canvas(object):
    def __init__(self, width, height, size):
        self.width = width
        self.height = height
        self.size = size
        pygame.init()
        self.screen = pygame.display.set_mode((width * size, height * size))

    def line(self, (x1, y1), (x2, y2), color=(0, 0, 0)):
        x1 *= self.size
        y1 *= self.size
        x2 *= self.size
        y2 *= self.size
        rect = pygame.draw.line(self.screen, color, (x1, y1), (x2, y2))
        pygame.display.update(rect)

    def rect(self, (x1, y1), (x2, y2), color=(255, 255, 255)):
        x1 *= self.size
        y1 *= self.size
        x2 *= self.size
        y2 *= self.size
        self.screen.fill(color, ((x1, y1), (x2, y2)))
        pygame.display.update(((x1, y1), (x2, y2)))
        
