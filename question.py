import random

class Question:

    #initializes a list of answers, a correct answer, the string for the question, and the image
    def __init__(self, answers, question, image):
        self.answers = answers
        self.correct = answers[0]
        self.question_text = question
        self.image = image
        random.shuffle(self.answers)
