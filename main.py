import math

import pygame
import sys
import random
from samples import board
import hole
import time
import instructionscreen


def main():
    hole.score = 0
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
    spawn_probability = 0.998  # ehh... sort of
    font = pygame.font.SysFont("papyrus", 32)
    the_board.spawn_counselor()
    click_pos = (0, 0)
    pygame.mouse.set_visible(True)
    cookie = pygame.image.load("Images/Cookie.png")
    cookie = pygame.transform.scale(cookie, (25, 25))
    cursor_img_rect = cookie.get_rect()
    start = pygame.image.load("Images/StartScreen")
    start = pygame.transform.scale(start, (screen_width, screen_height))
    win_image = pygame.image.load("Images/CookieRoyale")
    win_image = pygame.transform.scale(win_image, (screen_width, screen_height))
    loose_image = pygame.image.load("Images/Funished")
    loose_image = pygame.transform.scale(loose_image, (screen_width, screen_height))

    def start_screen():
        while True:
            for an_event in pygame.event.get():
                if an_event.type == pygame.QUIT:
                    sys.exit()
                if an_event.type == pygame.MOUSEBUTTONDOWN:
                    return

            screen.blit(start, (0, 0))
            pygame.display.update()

    start_screen()
    instructionscreen.instruction_screen(screen)
    pygame.mouse.set_visible(False)
    start_time = time.time()
    end_time = start_time + 45  # seconds

    while True:
        if time.time() > end_time:
            break
        clicked = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                click_pos = event.pos
                clicked = True
        if not clicked:
            click_pos = (0, 0)

            # TODO: Add you events code

        if random.random() > spawn_probability:
            the_board.spawn_counselor()
        screen.fill((175, 157, 255))
        the_board.update(click_pos)
        the_board.draw()
        # TODO: Add your project code

        # don't forget the update, otherwise nothing will show up!
        score_text = font.render(f"Score = {hole.score}", True, (0, 0, 0))
        time_text = font.render(f"Time: {math.ceil(end_time - time.time())}", True, (0, 0, 0))
        screen.blit(score_text, (0, 0))
        screen.blit(time_text, (screen_width - 200, 0))
        cursor_img_rect.center = pygame.mouse.get_pos()  # update position
        screen.blit(cookie, cursor_img_rect)

        pygame.display.update()
    pygame.mouse.set_visible(True)
    win_score = 4000
    if hole.score >= win_score:
        end_image = win_image
    else:
        end_image = loose_image
    clicked = False
    while not clicked:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                clicked = True

        screen.blit(end_image, (0, 0))
        pygame.display.update()


while True:
    main()
