import hole
import pygame
import random

# This is the board. It manages the holes.
class Board():
    def __init__(self, screen, background, rows, columns):
        self.screen = screen
        self.background = background
        self.rows = rows
        self.columns = columns
        self.counselor_images = []
        self.holes = []
        self.hole_radius = 50
        self.x_gap = (screen.get_width() - 100 * columns) // columns
        self.y_gap = (screen.get_height() - 100 * rows) // rows
        self.counselor_images = []
        for i in range(len(self.counselor_images)):
            self.counselor_images[i] = pygame.image.load(self.counselor_images[i])
        for i in range(rows):
            for j in range(columns):
                    x = self.x_gap + 2*i
                    y = self.y_gap + 2*j
                    self.holes.append(hole.Hole(self.screen, x, y, self.counselor_images, self.hole_radius))

    # This tells each hole to draw itself
    def draw(self):
        for hole in self.holes:
            hole.draw()

    # This tells an empty hole to spawn a counselor
    def spawn_counselor(self):
        hole = random.choice(self.holes)
        while hole.is_active:
            hole = random.choice(self.holes)
        hole.spawn()

