import pygame
import sys
import random
import time
import board


score = 0


def main():
    score = 0
    # turn on pygame
    pygame.init()
    # create a screen
    pygame.display.set_caption("Cookie A Counselor")
    screen_width = 1000
    screen_height = 600
    screen = pygame.display.set_mode((screen_width, screen_height))
    rows = 3
    columns = 4
    the_board = board.Board(screen, rows, columns)

    # let's set the frame rate
    clock = pygame.time.Clock()
    the_board.spawn_counselor()
    click_pos = (0,0)
    while True:
        clicked = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                click_pos = event.pos
                clicked = True
        if not clicked:
            click_pos = (0,0)

            # TODO: Add you events code

        screen.fill((172, 45, 201))
        the_board.update(click_pos)
        the_board.draw()#
        # TODO: Add your project code

        # don't forget the update, otherwise nothing will show up!
        pygame.display.update()



main()
