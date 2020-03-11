import pygame
import os
os.environ["SDL_VIDEO_WINDOW_POS"] = "15,30"

pygame.display.init()
screen = pygame.display.set_mode((600,600))

def draw_spiral():
    point = (300,300)
    pygame.draw.circle(screen, (255,255,255), point, 5)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    draw_spiral()
    pygame.display.update()
