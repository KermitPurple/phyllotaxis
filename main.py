import pygame
import os
from numpy import sin, cos, sqrt
os.environ["SDL_VIDEO_WINDOW_POS"] = "15,30"

pygame.display.init()
screen = pygame.display.set_mode((600,600))
rotating_angle = 0
circle_size = 3

def draw_spiral():
    for n in range(2000):
        theta = (n * 137.5 * 3.14159265)/180
        theta += rotating_angle
        r = 10 * sqrt(n)
        point = (int(r * cos(theta))+300, int(r * sin(theta))+300)
        color = pygame.Color(255,255,255)
        color.hsva = (n % 360, 100, 100)
        pygame.draw.circle(screen, color, point, circle_size)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.unicode == "+":
                circle_size += 1
            elif event.unicode == "-":
                circle_size -= 1
    screen.fill((0,0,0))
    draw_spiral()
    rotating_angle += 0.01
    pygame.display.update()
