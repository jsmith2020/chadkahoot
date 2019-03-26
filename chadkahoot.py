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
    ali_a_image = pygame.image.load
    ('ali-a.png')
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
    WWII_image = pygame.image.load('WWII.jpg')    global battle_of_the_bulge_image
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

def call_questions():
    global game_question1 = question(["Epic Games, Ubisoft, Mojang, Supercell"],"What studio created Fortnite?")
    global game_question2 = question(["Wailord, Pinkachu, Charzard, Calvin"], "Who is the biggest Pokemon?")
    global game_question3 = question(["Infinite Warfare, Fallout 76, Sim City 2013, Casey Powell Lacrosse 16"], "What video game trailer received the most amounts of dislikes on YouTube?")
    global game_question4 = question(["5 Minutes 58 Seconds, 4 minutes 3 seconds, 2 minutes 23 seconds, 7 minutes 49 seconds"], "What is the world record time for beating Super Mario Bros?")
    global game_question5 = question(["2013, 2012, 2014, 2011"], "When was the PS4 released?")
    global game_question6 = question(["2013, 2012, 2015, 2014"], "When was GTA V released?")
    global game_question7 = question(["2013, 2011, 2012, 2014"], "When was FIFA 14 released?")
    global game_question8 = question(["2012, 2013, 2011, 2014"], "When was CS:GO released?")
    global history_question1 = question(["1933, 1929, 1941, 1935"], "When did Hitler take power?")
    global history_question2 = question(["Mussolini, SpaghettMan, King Alfonso X, The Pope"], "Who was the leader of Italy during WW2?")
    global history_question3 = question(["1939, 1940, 1938, 1941"], "In what year did WW2 start?")
    global history_question4 = question(["Belgium, Netherlands, Koenburg, France"], "In what country was the battle of the bulge fought?")
    global history_question5 = question(["6 million, 600 thousand, 28 million, 1.2 million"], "How many people died in the invasion of china?")
    global history_question6 = question(["Nagasaki & Hiroshima, Tokyo and Okinawa, Iwo Jima and Hiroshima, Osaka and Nagasaki"], "In what Japanese cities were the first atomic bombs dropped?")
    global history_question7 = question(["Battle of the Atlantic, Battle of the Bulge, Battle of France, The Battle of the Bagel"], "What was the longest battle of WW2?")
    global history_question8 = question(["Dachau, Danzig, Auschwitz, Lodz"], "What was the first Nazi concentration camp?")
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


    meme_question1 = Question(["karen, the zucc, big chungus,koen"],"Who took the kids?",)
    meme_question2 = Question(["ninja, guy fieri, jeff bezos, mario"], "What internet personality died of Ligma?")
    meme_question3 = Question(["The Zucc Bot, Thomas,Johnny-Johnny,Patrick Star, Kazoo Kid"], "What internet person is a lizard?")
    meme_question4 = Question(["Knuckes, Motomoto, obiwan kanobi, Ali-A"], "What is the only noteable thing from Uganda?")
    meme_question5 = Question(["Spaghget, My soul, The magic school bus, Harry Truman"], "What did somebody ah-touch?")
    meme_question6 = Question(["Harambe, Gekyume, Jah, Thanos"], "Who forever lives in our hearts?")
    meme_question7 = Question(["Ali-A, Pewdiepie,Thomas Hudson, Mr. Kantaros"],"Who has a intro that will make your eardrums bleed")
    meme_question8 = Question(["Sugar, pancakes,Brown Sugar, Bread"], "What is Johnny-Johnny Eating?")

    sport_question1 = Question(["Yankees-27, Twins-13, Mets-15, Astros-4"], "What baseball team has the most world series wins?")
    sport_question2 = Question(["American Pharo, Zues,Thomas Hudson, African King"], "What was the last horse to win a triple crown?")
    sport_question3 = Question(["David Robinson, Michael Jordan, John Stockton, Jebron James"], "What NBA player was names 'the admiral'")
    sport_question4 = Question(["Antoine Walker, Allen Iverson, Shaq, Steph Curry"], "What player was on the cover of NBA 2K 99")
    sport_question5 = Question(["2500 mi, 1,500 mi, 2000 mi, 1000 mi"], "How long in the Tour De France?")
    sport_question6 = Question(["Jai alai, ping pong, cricket, baseball"], "What sport is this?")
    sport_question7 = Question(["Brazil, Argentina, Spain, Portugal"], "What is the only country to play in every world cup?")
    sport_question8 = Question(["Karren Abdul-Jabar, Michael Jordan, Kobe Bryant, Lebron James"],"Who is the all-time leading scorer in the NBA?"
