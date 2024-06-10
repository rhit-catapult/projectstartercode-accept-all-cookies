import pygame
import sys
import random
import time


score = 0


def main():
    score = 0
    # turn on pygame
    pygame.init()
    # create a screen
    pygame.display.set_caption("Cookie A Counselor")
    screen_width = 1000
    screen_height =600
    screen = pygame.display.set_mode((screen_width, screen_height))

    # let's set the frame rate
    clock = pygame.time.Clock()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            # TODO: Add you events code

        screen.fill((255, 255, 255))

        # TODO: Add your project code

        # don't forget the update, otherwise nothing will show up!
        pygame.display.update()


main()
