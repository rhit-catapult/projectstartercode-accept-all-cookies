import hole
import pygame
import random

# This is the board. It manages the holes.
class Board():
    def __init__(self, screen, rows, columns):
        self.screen = screen
        self.rows = rows
        self.columns = columns
        self.counselor_images = [
            "Images/Aaron.png", "Images/Anahita.png", "Images/Brayden.png", "Images/Claire.png",
            "Images/Eathan.png", "Images/Eli.png", "Images/Elley.png", "Images/Emmet.png",
            "Images/Fox.png", "Images/Hoyt.png", "Images/Kali.png", "Images/Micheal.png",
            "Images/Reid.png", "Images/Ruby.png", "Images/Sparks.png", "Images/Tyler.png"
        ]
        self.holes = []
        self.hole_radius = 50
        self.x_gap = (screen.get_width() - self.hole_radius * 2 * columns) / columns
        self.y_gap = (screen.get_height() - self.hole_radius * 2 * rows) / rows
        for i in range(len(self.counselor_images)):
            self.counselor_images[i] = pygame.image.load(self.counselor_images[i])
        for i in range(columns):
            for j in range(rows):
                    x = self.x_gap * (i + 0.5) + self.hole_radius * (1 + 2 * i)
                    y = self.y_gap * (j + 0.5) + self.hole_radius * (1 + 2 * j)
                    self.holes.append(hole.Hole(self.screen, x, y, self.counselor_images, self.hole_radius))

    # This tells each hole to draw itself
    def draw(self):
        for hole in self.holes:
            hole.draw()

    # This tells an empty hole to spawn a counselor#
    def spawn_counselor(self):
        hole = random.choice(self.holes)
        while hole.is_active:
            hole = random.choice(self.holes)
        hole.spawn()


    def update(self):
        for hole in self.holes:
            pass