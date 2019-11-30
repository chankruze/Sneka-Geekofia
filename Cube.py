import pygame


class Cube(object):
    rows = 50
    width = 500

    def __init__(self, start, color=(255, 0, 0)):
        self.position = start
        self.direction_x = 1
        self.direction_y = 0
        self.color = color

    def move(self, direction_x, direction_y):
        self.direction_x = direction_x
        self.direction_y = direction_y
        self.position = (self.position[0] + self.direction_x, self.position[1] + self.direction_y)

    def draw(self, surface, head=False):
        size = self.width // self.rows
        row = self.position[0]
        col = self.position[1]

        if head:
            pygame.draw.rect(surface, (255, 255, 255), (row * size, col * size, size, size))
        else:
            pygame.draw.rect(surface, self.color, (row * size + 1, col * size + 1, size - 2, size - 2))
