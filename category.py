import random
import pygame, sys, time, random
from pygame.locals import *

class Category:

    def __init__(self, questions):
        self.questions = questions
        self.question = self.questions[random.randint(0, len(self.questions) - 1)]

    def display_text(self, DISPLAYSURF):
        BASICFONT = pygame.font.Font('Roboto-Black.ttf', 16)
        Surf = BASICFONT.render(self.question.question_text, 1, (0,0,0))
        Rect = Surf.get_rect()
        Rect.topleft = (350, 50)
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
        DISPLAYSURF.blit(self.question.image, (250, 100))


    def check_answer(self, click):
        if self.question.answers[click - 1] == self.question.correct:
            return True
        else:
            return False

    def new_question(self):
        self.questions.remove(self.question)
        self.question = self.questions[random.randint(0, len(self.questions) - 1)]
