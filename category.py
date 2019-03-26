import random
class Category:

    def __init__(self, questions):
        self.questions = questions
        self.question = self.questions[random.randint(0, len(self.questions) - 1)]

    def display_text(self):
        BASICFONT = pygame.font.Font('timesnewroman.ttf', 16)
        Surf = BASICFONT.render(self.question.question_text, 1, (0,0,0))
        Rect = Surf.get_rect()
        Rect.topleft = (350, 150)
        DISPLAYSURF.blit(Surf, Rect)
        Surf = BASICFONT.render(self.question.answers[0], 1, (0,0,0))
        Rect = Surf.get_rect()
        Rect.topleft = (150, 375)
        DISPLAYSURF.blit(Surf, Rect)
        Surf = BASICFONT.render(self.question.answers[1], 1, (0,0,0))
        Rect = Surf.get_rect()
        Rect.topleft = (150, 525)
        DISPLAYSURF.blit(Surf, Rect)
        Surf = BASICFONT.render(self.question.answers[2], 1, (0,0,0))
        Rect = Surf.get_rect()
        Rect.topleft = (450, 375)
        DISPLAYSURF.blit(Surf, Rect)
        Surf = BASICFONT.render(self.question.answers[3], 1, (0,0,0))
        Rect = Surf.get_rect()
        Rect.topleft = (150, 425)
        DISPLAYSURF.blit(Surf, Rect)


    def check_answer(self, click):
        if self.question.answers[click - 1] == self.question.correct:
            return True
        else:
            return False

    def new_question(self):
        self.questions.remove(self.question)
        self.question = self.questions[random.randint(0, len(self.questions) - 1)]

#jake's questions
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
    sport_question8 = Question(["Karren Abdul-Jabar, Michael Jordan, Kobe Bryant, Lebron James"],"Who is the all-time leading scorer in the NBA?")
    #after last comma add image
