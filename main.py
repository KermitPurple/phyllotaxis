import pygame
import os
from numpy import sin, cos, sqrt
os.environ["SDL_VIDEO_WINDOW_POS"] = "15,30"

pygame.display.init()
screen = pygame.display.set_mode((600,600))
rotating_angle = 0

def draw_spiral():
    for n in range(2000):
        theta = (n * 137.5 * 3.14159265)/180
        theta += rotating_angle
        r = 10 * sqrt(n)
        point = (int(r * cos(theta))+300, int(r * sin(theta))+300)
        pygame.draw.circle(screen, (255,255,255), point, 5)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    draw_spiral()
    rotating_angle += 0.001
    pygame.display.update()
