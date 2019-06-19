'''--------------------------------------------------------------
--------------------- PyGame으로 원 그리기 ---------------------------
--------------------------------------------------------------'''

import pygame, sys
from pygame.locals import *

pygame.init()

windowSurface = pygame.display.set_mode((500, 400), 0, 32)
pygame.display.set_caption("안녕")

windowSurface.fill((255,255,255))

pygame.draw.circle(windowSurface , (255,255,0), (250,50), 50, 0)

pygame.display.update()

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()