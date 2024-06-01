from question_model import qna_list
import random


class QuizBrain:
    def __init__(self):
        self.remaining_questions = qna_list.copy()  # stores details of questions not asked
        self.ques_picked = None  # stores details of currently asked question
        self.answer = None  # stores answer of currently asked question
        self.input_answer = None  # stores answer given by the user
        self.ques_number = 0  # stores current question number
        self.score = 0  # stores current score

    def ask_question(self):
        """
        generates new question and ask that to user
        """
        self.ques_picked = random.choice(self.remaining_questions)
        self.remaining_questions.remove(self.ques_picked)
        self.ques_number += 1
        self.answer = self.ques_picked.answer
        # self.ques_asked.append(self.ques_picked.text)
        print(f'Q.{self.ques_number}: {self.ques_picked.text} (True/False)?')

    def get_answer(self):
        """
        takes user answer as input
        """
        while True:
            self.input_answer = input().lower()
            if self.input_answer in {'true', 'false'}:
                break
            else:
                print("Enter valid input: True/False")

    def check_answer(self):
        """
        checks if the answer given by user is correct
        """
        if self.input_answer == self.answer:
            self.score += 1
            print("You got it right!")
        else:
            print("That's wrong!")
        print(f"The correct answer was: {self.answer}\nYour current score is: {self.score}/{self.ques_number}")

    def is_end(self):
        """
        checks if all questions have been asked
        """
        if not self.remaining_questions:
            print(f"\nQUIZ OVER!!!!!\nYour final score is: {self.score}/{self.ques_number}")
            return True

    def play_quiz(self):
        """
        steps to play quiz
        """
        while not self.is_end():
            self.ask_question()
            self.get_answer()
            self.check_answer()
