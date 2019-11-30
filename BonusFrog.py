import pygame


class BonusFrog(object):
    rows = 50

    def __init__(self, position, debug=False):
        self.flag = False
        self.position = position
        self.color = (0, 200, 255)

        if debug:
            print("== New Frog ==")
            print("row", self.position[0], "(", self.position[0] * self.rows, "px)")
            print("col", self.position[1], "(", self.position[1] * self.rows, "px)")
            print("==========")

    def hide(self, surface, color):
        surface.set_at(self.position, color)

    def span(self, surface):
        size = surface.get_size()[0] // self.rows
        row = self.position[0]
        col = self.position[1]

        pygame.draw.rect(surface, self.color, (row * size, col * size, size, size))

    def should_span(self, stat):
        if stat:
            self.flag = True
        else:
            self.flag = False

    def is_spanned(self):
        return self.flag
