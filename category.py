import random
class Category:

    def __init__(self, questions):
        self.questions = questions
        self.question = self.questions[random.randint(0, len(self.questions) - 1)]

    def display_tex(self):
        print()

    def check_answer(self, click):
        if self.question.answers[click - 1] == self.question.correct:
            return True
        else:
            return False

    def new_question(self):
        self.questions.remove(self.question)
        self.question = self.questions[random.randint(0, len(self.questions) - 1)]
