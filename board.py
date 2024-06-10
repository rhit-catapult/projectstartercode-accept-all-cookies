import hole
import pygame

class Board():
    def __init__(self, screen, background, rows, columns):
        self.screen = screen
        self.background = background
        self.rows = rows
        self.columns = columns
        self.counselor_images =[]
        self.holes=[]
        