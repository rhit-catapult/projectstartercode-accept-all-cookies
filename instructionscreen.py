import pygame
import sys


def instruction_screen(screen):
    instruction_screen_image = pygame.image.load("Images/Instructions.png")
    instruction_screen_image = pygame.transform.scale(instruction_screen_image,
                                                      (screen.get_width(), screen.get_height()))
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                return

        screen.blit(instruction_screen_image, (0, 0))
        pygame.display.update()
