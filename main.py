import pygame
from pygame import quit
from sys import exit
from settings import *
from human import Human

pygame.init()

clock = pygame.time.Clock()

screen = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption("refactored conscious")

test_human = Human("john","smith","warrior",20,100)
human_group = pygame.sprite.Group()
human_group.add(test_human)

while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			quit()
			exit()
	# screen.fill("white")
	human_group.draw(screen)
	pygame.display.flip()
	clock.tick(60)
