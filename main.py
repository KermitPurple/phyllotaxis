import pygame
import os
from numpy import sin, cos, sqrt
os.environ["SDL_VIDEO_WINDOW_POS"] = "15,30"

pygame.display.init()
size = 650
screen = pygame.display.set_mode((size,size))
rotating_angle = 0
c = 10
circle_size = 5
points = 2300
special_angle = 137.5

def draw_spiral():
	for n in range(points):
		theta = (n * special_angle * 3.14159265)/180
		theta += rotating_angle
		r = c * sqrt(n)
		point = (int(r * cos(theta))+int(size/2), int(r * sin(theta))+int(size/2))
		color = pygame.Color(255,255,255)
		color.hsva = (n % 360, 100, 100)
		pygame.draw.circle(screen, color, point, circle_size)

running = True
pygame.key.set_repeat(80)
while running:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
		if event.type == pygame.KEYDOWN:
			if event.unicode == "+":
				circle_size += 1
			elif event.unicode == "-":
				if circle_size > 1:
					circle_size -= 1
			elif event.unicode == '1':
				c = 3
				circle_size = 1
				points = 15000
			elif event.unicode == '2':
				c = 10
				circle_size = 5
				points = 2500
			elif event.unicode == ',':
				special_angle -= 0.1
				if special_angle < 0:
					special_angle = 0
			elif event.unicode == '.':
				special_angle += 0.1
				if special_angle > 360:
					special_angle = 360
			elif event.unicode == 'k':
				special_angle -= 0.5
				if special_angle < 0:
					special_angle = 0
			elif event.unicode == 'l':
				special_angle += 0.5
				if special_angle > 360:
					special_angle = 360
			elif event.unicode == '=':
				special_angle = 137.5
			elif event.unicode == 'p':
				print("special angle:",special_angle)
	screen.fill((0,0,0))
	draw_spiral()
	rotating_angle += 0.01
	pygame.display.update()
