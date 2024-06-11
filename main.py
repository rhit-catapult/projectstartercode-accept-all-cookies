import pygame
import sys
import random
from Images import board
import hole



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
    spawn_probabily = 0.998 #ehh... sort of
    font = pygame.font.SysFont("papyrus", 32)

    #TODO add start screen


    # let's set the frame rate
    clock = pygame.time.Clock()
    the_board.spawn_counselor()
    click_pos = (0,0)
    pygame.mouse.set_visible(True)
    cookie = pygame.image.load("Images/Cookie.png")
    cookie = pygame.transform.scale(cookie, (25, 25))
    cursor_img_rect = cookie.get_rect()
    start = pygame.image.load("Images/StartScreen")
    start = pygame.transform.scale(start, (screen_width, screen_height))

    def startstive():
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    return
            screen.fill((172, 45, 201))

            screen.blit(start, (0, 0))
            pygame.display.update()
            if random.random() > 0.99999:
                break
        pygame.mouse.set_visible(False)

    startstive()

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

        if random.random() > spawn_probabily:
            the_board.spawn_counselor()
        screen.fill((172, 45, 201))
        the_board.update(click_pos)
        the_board.draw()
        # TODO: Add your project code

        # don't forget the update, otherwise nothing will show up!
        text = font.render(f"Score = {hole.score}", True, (0, 0, 0))
        screen.blit(text, (0,0))
        cursor_img_rect.center = pygame.mouse.get_pos()  # update position
        screen.blit(cookie, cursor_img_rect)

        pygame.display.update()


main()
