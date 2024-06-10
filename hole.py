import pygame
import sys
import random
import time
import math


def main():
    #main function! for debugging purposes
    pass


def distance(point1, point2):
    point1_x = point1[0]
    point1_y = point1[1]
    point2_x = point2[0]
    point2_y = point2[1]

    delta_x = point2_x - point1_x
    delta_y = point2_y - point1_y
    dist = math.sqrt(delta_x ** 2 + delta_y ** 2)

    return dist


class Hole:
    #recieves information from the board, initializes holes
    def __init__(self, screen, x, y, counselor_images, radius):
        self.screen = screen
        self.x = x #center circle x coord
        self.y = y #center circle y coord
        self.counselor_images = counselor_images #counselor images
        self.radius = radius #radius of hole
        self.is_active = False #is there a counselor in the hole
        self.start_time = -1.0 #-1.0 when is_active is False, otherwise the most recent activation time\
        self.current_counselor = None
        self.end_time = 0.0
        print(self.counselor_images)


    #takes no input
    #returns boolean value - true if clicked, false otherwise
    def is_clicked(self):
        circle_center = (self.x, self.y)
        circle_radius = self.radius

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                click_pos = event.pos
                distance_from_circle = distance(circle_center, click_pos)

                return distance_from_circle <= circle_radius and self.is_active
        return False


        #TODO this hasn't actually been written yet
    def spawn(self):
        #spawns the counselor
        self.current_counselor = random.choice(self.counselor_images)
        self.counselor_images.remove(self.current_counselor)
        self.start_time = time.time()
        self.is_active = True

    def despawn(self, ate_cookie):
        self.is_active = False
        self.counselor_images.append(self.current_counselor)
        if not ate_cookie:
            #TODO add code to play scream
            pass
        else:
            #TODO add code to play eating sound
            pass





    def draw(self):
        pygame.draw.circle(self.screen, (0, 0, 0), (self.x, self.y), self.radius)

        if self.is_active:
            self.screen.blit(self.current_counselor, (self.x - self.radius, self.y - self.radius))


