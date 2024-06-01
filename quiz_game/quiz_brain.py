from question_model import qna_list
import random


class QuizBrain:
    def __init__(self):
        self.ques_picked = None
        self.answer = None
        self.input_answer = None
        self.ques_asked = []
        self.ques_number = 0
        self.score = 0

    def is_question_asked(self, ques):
        for data in self.ques_asked:
            if data == ques:
                return True

    def ask_question(self):
        if self.ques_number == 0:
            self.ques_picked = random.choice(qna_list)
        else:
            while self.is_question_asked(self.ques_picked.text):
                self.ques_picked = random.choice(qna_list)
        self.ques_number += 1
        self.answer = self.ques_picked.answer
        self.ques_asked.append(self.ques_picked.text)
        print(f'{self.ques_picked.text} (True/False)?')
        return self.ques_asked

    def is_end(self):
        if len(qna_list) == len(self.ques_asked):
            print(f"\nQUIZ OVER!!!!!\nYour final score is: {self.score}/{self.ques_number}")
            return True

    def get_answer(self):
        while True:
            self.input_answer = input().lower()
            if self.input_answer in {'true', 'false'}:
                break
            else:
                print("Enter valid input: True/False")

    def check_answer(self):
        if self.input_answer == self.answer:
            self.score += 1
            print("You got it right!")
        else:
            print("That's wrong!")
        print(f"The correct answer was: {self.answer}\nYour current score is: {self.score}/{self.ques_number}")

    def calculate_score(self):
        pass
