import pygame, sys, time, random
from pygame.locals import *
pygame.init()

DISPLAYSURF = pygame.display.set_mode((800, 600))
pygame.display.set_caption("KAHOOT")

FPS = 50
fpsClock = pygame.time.Clock()

RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

def ask_question(color):
    frametime = 0
    if frametime <= 1000:
        frametime = frametime + 1
        if category.check_answer(color):
            return 1000 - frametime
        else:
            return 0
    else:
        return 0

def draw_shapes():
    pygame.draw.rect(DISPLAYSURF, WHITE, (0, 0, 800, 300))
    pygame.draw.rect(DISPLAYSURF, GREEN, (0, 300, 400, 150))
    pygame.draw.rect(DISPLAYSURF, RED, (400, 300, 400, 150))
    pygame.draw.rect(DISPLAYSURF, YELLOW, (0, 450, 400, 150))
    pygame.draw.rect(DISPLAYSURF, BLUE, (400, 450, 400, 150))
    pygame.draw.line(DISPLAYSURF, BLACK, (400, 300), (400, 600), 5)
    pygame.draw.line(DISPLAYSURF, BLACK, (0, 450), (800, 450), 5)
    pygame.draw.line(DISPLAYSURF, BLACK, (0, 0), (800, 0), 5)
    pygame.draw.line(DISPLAYSURF, BLACK, (0, 0), (0, 600), 5)
    pygame.draw.line(DISPLAYSURF, BLACK, (0, 600), (800, 600), 5)
    pygame.draw.line(DISPLAYSURF, BLACK, (800, 0), (800, 600), 5)
    pygame.draw.line(DISPLAYSURF, BLACK, (0, 300), (800, 300), 5)

def assign_color(click):
    if click[0] < 401 and click[1] > 300:
        if click[1] < 451:
            return 1
        else:
            return 3
    elif click[0] > 401 and click[1] > 300:
        if click[1] < 451:
            return 2
        else:
            return 4

click = (-1, -1)
color = False
while True:
    for event in pygame.event.get():

        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        if event.type == MOUSEBUTTONDOWN:
            click = pygame.mouse.get_pos()
            color = assign_color(click)

    draw_shapes()
    pygame.display.update()
