import pygame, sys, time, random
from pygame.locals import *
pygame.init()

DISPLAYSURF = pygame.display.set_mode((800, 600))
pygame.display.set_caption("KAHOOT")

pygame.mixer.music.load('kahootmusic.mp3')
pygame.mixer.music.play(-1, 0.0)

FPS = 50
fpsClock = pygame.time.Clock()

RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
UGLY = (250, 0, 150)

def load_images():
    global kahoot_image
    karen_image = pygame.image.load('kid-suitcase.jpg')
    global ligma_image
    ligma_image = pygame.image.load('ligma.jpg')
    global lizard_image
    lizard_image = pygame.image.load('lizard.jpg')
    global knuckles_image
    knuckles_image = pygame.image.load('knuckles.jpg')
    global harambe_image
    harambe_image = pygame.image.load('harambe.jpg')
    global spaghet_image
    spaghet_image = pygame.image.load('spaghet.jpg')
    global ali_a_image
    ali_a_image = pygame.image.load('ali-a.png')
    global johnny_image
    johnny_image = pygame.image.load('johnny.jiff')
    global fortnite_image
    fortnite_image = pygame.image.load('fortnite.png')
    global pokemon_image
    pokemon_image = pygame.image.load('pokemon.jpg')
    global dislike_image
    dislike_image = pygame.image.load('dislike.jiff')
    global mario_image
    mario_image = pygame.image.load('mario.jpg')
    global PS4_image
    PS4_image = pygame.image.load('PS4.jpeg')
    global gtav_image
    gtav_image = pygame.image.load('gtav.jpg')
    global fifa_image
    fifa_image = pygame.image.load('fifa-14.jpg')
    global csgo_image
    csgo_image = pygame.image.load('csgo.jpg')
    global hitler_image
    hitler_image = pygame.image.load('gitler.jpg')
    global mussolini_image
    mussolini_image = pygame.image.load('mussolini.jpg')
    global WWII_image
    WWII_image = pygame.image.load('WWII.jpg')
    global battle_of_the_bulge_image
    battle_of_the_bulge_image = pygame.image.load('battle_of_the_bulge.jpg')
    global invasion_of_china_image
    invasion_of_china_image = pygame.image.load('invasion_of_china.jpg')
    global battle_of_atlantic_image
    battle_of_atlantic_image = pygame.image.load('atlantic-battle.jpg')
    global dachau_image
    dachau_image = pygame.image.load('dachau.jpeg')
    global world_series_image
    world_series_image = pygame.image.load('world_series.png')
    global horse_image
    horse_image = pygame.image.load('horse.jpg')
    global admiral_image
    admiral_image = pygame.image.load('admial.png')
    global NBA_2K_image
    NBA_2K_image = pygame.image.load('2K.jpg')
    global tour_de_france_image
    tour_de_france_image = pygame.image.load('tour_de_france.jpg')
    global jai_alai_image
    jai_alai_image = pygame.image.load('jai_alai.jpg')
    global world_cup_image
    world_cup_image = pygame.image.load('world_cup.jpg')

def ask_question(color):
    frametime = 0
    if frametime <= 1000:
        frametime = frametime + 1
        pygame.draw.line(DISPLAYSURF, UGLY, (0, 50), (frametime, 50), 15)
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
        while num <= 8:
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                click = pygame.mouse.get_pos()
                color = assign_color(click)

    draw_shapes()
    pygame.display.update()
