import pygame, sys, time, random
from pygame.locals import *
from question import Question
from category import Category

pygame.init()
#Contains the Images for Each Question and Makes them into Global Variables
def load_images():
    global karen_image
    karen_image = pygame.image.load('images/kid-suitcase.jpg')
    global ligma_image
    ligma_image = pygame.image.load('images/ligma.jpg')
    global lizard_image
    lizard_image = pygame.image.load('images/lizard.jpg')
    global knuckles_image
    knuckles_image = pygame.image.load('images/knuckles.jpg')
    global harambe_image
    harambe_image = pygame.image.load('images/harambe.jpg')
    global spaghet_image
    spaghet_image = pygame.image.load('images/spaghet.jpg')
    global ali_a_image
    ali_a_image = pygame.image.load('images/ali-a.png')
    global johnny_image
    johnny_image = pygame.image.load('images/johnny.png')
    global fortnite_image
    fortnite_image = pygame.image.load('images/fortnite.png')
    global pokemon_image
    pokemon_image = pygame.image.load('images/pokemon.jpg')
    global dislike_image
    dislike_image = pygame.image.load('images/dislike.png')
    global mario_image
    mario_image = pygame.image.load('images/mario.jpg')
    global PS4_image
    PS4_image = pygame.image.load('images/PS4.jpeg')
    global gtav_image
    gtav_image = pygame.image.load('images/gtav.jpg')
    global fifa_image
    fifa_image = pygame.image.load('images/fifa-14.jpg')
    global csgo_image
    csgo_image = pygame.image.load('images/csgo.jpg')
    global hitler_image
    hitler_image = pygame.image.load('images/hitler.jpg')
    global mussolini_image
    mussolini_image = pygame.image.load('images/mussolini.jpg')
    global WWII_image
    WWII_image = pygame.image.load('images/WWII.jpg')
    global battle_of_the_bulge_image
    battle_of_the_bulge_image = pygame.image.load('images/battle_of_the_bulge.jpg')
    global invasion_of_china_image
    invasion_of_china_image = pygame.image.load('images/invasion_of_china.jpg')
    global battle_of_atlantic_image
    battle_of_atlantic_image = pygame.image.load('images/atlantic-battle.jpg')
    global dachau_image
    dachau_image = pygame.image.load('images/dachau.jpeg')
    global world_series_image
    world_series_image = pygame.image.load('images/world_series.png')
    global horse_image
    horse_image = pygame.image.load('images/horse.jpg')
    global admiral_image
    admiral_image = pygame.image.load('images/admiral.png')
    global NBA_2K_image
    NBA_2K_image = pygame.image.load('images/2K.jpg')
    global tour_de_france_image
    tour_de_france_image = pygame.image.load('images/tour_de_france.jpg')
    global jai_alai_image
    jai_alai_image = pygame.image.load('images/jai_alai.jpg')
    global world_cup_image
    world_cup_image = pygame.image.load('images/world_cup.jpg')
    global atomic_image
    atomic_image = pygame.image.load('images/atomic_bomb.jpg')
#Checks the Answer to make sure its correct or incorrect and loads the progress bar
def ask_question(color, category, frametime):
    #Runs while the Game is still within the time limit
    if frametime <= 1000:
        #creates the progress bar
        pygame.draw.line(DISPLAYSURF, WHITE, (1000, 0), (1000 - frametime, 0), 30)
        #Checks answer based upon the color
        if color > 0:
            if category.check_answer(color):
                return 1000 - frametime
            else:
                return 0
        else:
            return -1
    else:
        global answered
        answered = True
        return 0
#Contains the Question classes with corresponding image variables
def call_questions():
    #Creates the gaming related question classes; the first answer in the list is the correct one. It also lists the image corresponding to each question.
    game_question1 = Question(["Epic Games", "Ubisoft", "Mojang", "Supercell"], "What studio created Fortnite?", fortnite_image)
    game_question2 = Question(["Wailord", "Pikachu", "Charzard", "Calvin"], "Who is the biggest Pokemon?", pokemon_image)
    game_question3 = Question(["Infinite Warfare", "Fallout 76", "Sim City 2013", "Casey Powell Lacrosse 16"], "What video game trailer received the most amounts of dislikes on YouTube?", dislike_image)
    game_question4 = Question(["5 Minutes 58 Seconds", "4 minutes 3 seconds", "2 minutes 23 seconds", "7 minutes 49 seconds"], "What is the world record time for beating Super Mario Bros?", mario_image)
    game_question5 = Question(["2013", "2012", "2014", "2011"], "When was the PS4 released?", PS4_image)
    game_question6 = Question(["2013", "2012", "2015", "2014"], "When was GTA V released?", gtav_image)
    game_question7 = Question(["2013", "2011", "2012", "2014"], "When was FIFA 14 released?", fifa_image)
    game_question8 = Question(["2012", "2013", "2011", "2014"], "When was CS:GO released?", csgo_image)
    #Creates WW2 related question classes; the first answer in the list is the correct one. It also lists the image corresponding to each question.
    history_question1 = Question(["1933", "1929", "1941", "1935"], "When did Hitler take power?", hitler_image)
    history_question2 = Question(["Mussolini", "SpaghettMan", "King Alfonso X", "The Pope"], "Who was the leader of Italy during WW2", mussolini_image)
    history_question3 = Question(["1939", "1940", "1938", "1941"], "In what year did WW2 start?", WWII_image)
    history_question4 = Question(["Belgium", "Netherlands", "Koenburg", "France"], "In what country was the battle of the bulge fought?", battle_of_the_bulge_image)
    history_question5 = Question(["6 million", "600 thousand", "28 million", "1.2 million"], "How many people died in the invasion of china?", invasion_of_china_image)
    history_question6 = Question(["Nagasaki & Hiroshima", "Tokyo and Okinawa", "Iwo Jima and Hiroshima", "Osaka and Nagasaki"], "In what Japanese cities were the first atomic bombs dropped?", atomic_image)
    history_question7 = Question(["Battle of the Atlantic", "Battle of the Bulge", "Battle of France", "The Battle of the Bagel"], "What was the longest battle of WW2?", battle_of_atlantic_image)
    history_question8 = Question(["Dachau", "Danzig", "Auschwitz", "Lodz"], "What was the first Nazi concentration camp?", dachau_image)
    #Creates Meme related question classes; the first answer in the list is the correct one. It also lists the image corresponding to each question.
    meme_question1 = Question(["Karen", "The Zucc", "Big Chungus", "Koen"], "Who took the kids?", karen_image)
    meme_question2 = Question(["ninja", "guy fieri", "jeff bezos", "mario"], "What internet personality died of Ligma?", ligma_image)
    meme_question3 = Question(["The Zucc Bot", "Thomas", "Johnny-Johnny", "Patrick Star", "Kazoo Kid"], "What internet personality is a lizard?", lizard_image)
    meme_question4 = Question(["Knuckes", "Motomoto", "Obi-Wan Kanobi", "Ali-A"], "What is the only noteable meme from Uganda?", knuckles_image)
    meme_question5 = Question(["Spaghget", "My soul", "The magic school bus", "Harry Truman"], "What did somebody ah-touch?", spaghet_image)
    meme_question6 = Question(["Harambe", "Gekyume", "Jah", "Thanos"], "Who forever lives in our hearts?", harambe_image)
    meme_question7 = Question(["Ali-A", "Pewdiepie", "Thomas Hudson", "Mr. Kantaros"], "Who has a intro that will make your eardrums bleed?", ali_a_image)
    meme_question8 = Question(["Sugar", "Pancakes", "Brown Sugar", "Bread"], "What is Johnny-Johnny Eating?", johnny_image)
    #Creates Sports related question classes; the first answer in the list is the correct one. It also lists the image corresponding to each question.
    sport_question1 = Question(["Yankees-27", "Twins-13", "Mets-15", "Astros-4"], "What baseball team has the most world series wins?", world_series_image)
    sport_question2 = Question(["American Pharo", "Zues", "Thomas Hudson", "African King"], "What was the last horse to win a triple crown?", horse_image)
    sport_question3 = Question(["David Robinson", "Michael Jordan", "John Stockton", "Jebron James"], "What NBA player was names 'the admiral'", admiral_image)
    sport_question4 = Question(["Antoine Walker", "Allen Iverson", "Shaq", "Steph Curry"], "What player was on the cover of NBA 2K 99", NBA_2K_image)
    sport_question5 = Question(["2500 mi", "1,500 mi", "2000 mi", "1000 mi"], "How long in the Tour De France?", tour_de_france_image)
    sport_question6 = Question(["Jai alai", "Ping Pong", "Cricket", "Baseball"], "What sport is this?", jai_alai_image)
    sport_question7 = Question(["Brazil", "Argentina", "Spain", "Portugal"], "What is the only country to play in every world cup?", world_cup_image)
    sport_question8 = Question(["Karren Abdul-Jabar", "Michael Jordan", "Kobe Bryant", "Lebron James"], "Who is the all-time leading scorer in the NBA?", NBA_2K_image)
    #Turns all the categories into global variables and creates the category lists
    global sports
    global memes
    global history
    global games
    global categories
    sports = Category([sport_question1, sport_question2, sport_question3, sport_question4, sport_question5, sport_question6, sport_question7, sport_question8])
    memes = Category([meme_question1, meme_question2, meme_question3, meme_question4, meme_question5, meme_question6, meme_question7, meme_question8])
    history = Category([history_question1, history_question2, history_question3, history_question4, history_question5, history_question6, history_question7, history_question8])
    games = Category([game_question1, game_question2, game_question3, game_question4, game_question5, game_question6, game_question7, game_question8])
    categories = [sports, memes, history, games]

def draw_shapes():
    #Creates the game screen by drawing each corner of the screen in a different color, and seperating each color by a black line. It also creates the font to be used for the game and renders the score in the corner of the screen.
    pygame.draw.rect(DISPLAYSURF, WHITE, (0, 15, 800, 300))
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
    BASICFONT = pygame.font.Font('Roboto-Black.ttf', 16)
    Surf = BASICFONT.render(str(total_score), 1, (0,0,0))
    Rect = Surf.get_rect()
    Rect.topleft = (760, 20)
    DISPLAYSURF.blit(Surf, Rect)
#As
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
    else:
        return 0
#Displays the Correct Screen that fills the screen with green and prints correct
def correct_answer():
    DISPLAYSURF.fill(GREEN)
    BASICFONT = pygame.font.Font('Roboto-Black.ttf', 50)
    Surf = BASICFONT.render("CORRECT!", 1, (0,0,0))
    Rect = Surf.get_rect()
    Rect.topleft = (300, 200)
    DISPLAYSURF.blit(Surf, Rect)
    pygame.display.update()
    time.sleep(2)
    DISPLAYSURF.fill(UGLY)
#Displays the Incorrect Screen which fills the screen with red and prints incorrect
def incorrect_answer():
    DISPLAYSURF.fill(RED)
    BASICFONT = pygame.font.Font('Roboto-Black.ttf', 50)
    Surf = BASICFONT.render("INCORRECT!", 1, (0,0,0))
    Rect = Surf.get_rect()
    Rect.topleft = (300, 200)
    DISPLAYSURF.blit(Surf, Rect)
    pygame.display.update()
    time.sleep(2)
    DISPLAYSURF.fill(UGLY)
#Creates the game window, titles it, and begins to play the background music. It also creates most of the global variables including those relating to colors, the score, and FPS.
def make_variables():
    global DISPLAYSURF
    DISPLAYSURF = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("KAHOOT")

    pygame.mixer.music.load('kahootremix.mp3')
    pygame.mixer.music.play(-1, 0.0)

    global RED
    RED = (255, 0, 0)
    global GREEN
    GREEN = (0, 255, 0)
    global BLUE
    BLUE = (0, 0, 255)
    global YELLOW
    YELLOW = (255, 255, 0)
    global BLACK
    BLACK = (0, 0, 0)
    global WHITE
    WHITE = (255, 255, 255)
    global UGLY
    UGLY = (250, 0, 150)

    global click
    click = (-1, -1)
    global color
    color = False
    global total_score
    total_score = 0
    load_images()
    call_questions()
    global category
    category = categories[random.randint(0, 3)]
    global frametime
    frametime = 0
    DISPLAYSURF.fill(UGLY)
    global answered
    answered = False
    global FPS
    FPS = 60
    global fpsClock
    fpsClock = pygame.time.Clock()

make_variables()
#The Game Loop; contains and calls all the functions over the course of the game.
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == MOUSEBUTTONDOWN:
            click = pygame.mouse.get_pos()
            color = assign_color(click)
            answered = True

    score = ask_question(color, category, frametime)
    total_score += score
    frametime += 1
    if score > 0 and answered:
        category.new_question()
        DISPLAYSURF.fill(UGLY)
        frametime = 0
        answered = False
        color = -1
        correct_answer()
        category = categories[random.randint(0, 3)]
    elif score < 0:
        total_score += 1
    elif score == 0 and answered:
        category.new_question()
        DISPLAYSURF.fill(UGLY)
        frametime = 0
        answered = False
        color = -1
        incorrect_answer()
        category = categories[random.randint(0, 3)]

    draw_shapes()
    category.display_text(DISPLAYSURF)
    fpsClock.tick(FPS)
    pygame.display.update()
