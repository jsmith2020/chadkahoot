import pygame, sys, time, random
from pygame.locals import *

class Category:

#initializes the list of questions and randomly selects one to start with
    def __init__(self, questions):
        self.questions = questions
        self.question = self.questions[random.randint(0, len(self.questions) - 1)]

#Displays all the text on the screen, including the question, the four potential answers, and the image associated with each question.
    def display_text(self, DISPLAYSURF):
        BASICFONT = pygame.font.Font('Roboto-Black.ttf', 16)
        Surf = BASICFONT.render(self.question.question_text, 1, (0,0,0))
        Rect = Surf.get_rect()
        Rect.topleft = (200, 20)
        DISPLAYSURF.blit(Surf, Rect)
        Surf = BASICFONT.render(self.question.answers[0], 1, (0,0,0))
        Rect = Surf.get_rect()
        Rect.topleft = (100, 375)
        DISPLAYSURF.blit(Surf, Rect)
        Surf = BASICFONT.render(self.question.answers[1], 1, (0,0,0))
        Rect = Surf.get_rect()
        Rect.topleft = (450, 375)
        DISPLAYSURF.blit(Surf, Rect)
        Surf = BASICFONT.render(self.question.answers[2], 1, (0,0,0))
        Rect = Surf.get_rect()
        Rect.topleft = (100, 525)
        DISPLAYSURF.blit(Surf, Rect)
        Surf = BASICFONT.render(self.question.answers[3], 1, (0,0,0))
        Rect = Surf.get_rect()
        Rect.topleft = (450, 525)
        DISPLAYSURF.blit(Surf, Rect)
        DISPLAYSURF.blit(self.question.image, (100, 45))

    #removes the previous question, and compares the user's answer to the correct answer
    def check_answer(self, click):
        self.questions.remove(self.question)
        if self.question.answers[click - 1] == self.question.correct:
            return True
        else:
            return False

    #randomly selects a new question
    def new_question(self):
        if len(self.questions) > 0:
            self.question = self.questions[random.randint(0, len(self.questions) - 1)]
