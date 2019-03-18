import random

class Question:

    def __init__(self, answers, question, image):
        self.answers = answers
        self.correct = answers[0]
        self.question_text = question
        self.image = image
        random.shuffle(self.answers)
