import random


class QuizBrain:
    def __init__(self, ques_list):
        self.remaining_questions = ques_list.copy()  # stores details of questions not asked
        self.ques_number = 0  # stores current question number
        self.score = 0  # stores current score

    def next_question(self):
        """
        generates new question, takes user input and returns generated question answer and user input
        """
        ques_picked = random.choice(self.remaining_questions)
        self.remaining_questions.remove(ques_picked)
        self.ques_number += 1
        while True:
            input_ans = input(f"Q.{self.ques_number}: {ques_picked.text} (True/False)?: ").lower()
            if input_ans in {'true', 'false'}:
                break
            else:
                print("Enter valid input: True/False")
        return ques_picked.answer, input_ans

    def check_answer(self, ques_ans, input_ans):
        """
        checks if the answer given by user is correct
        """
        if input_ans == ques_ans:
            self.score += 1
            print("You got it right!")
        else:
            print("That's wrong!")
        print(f"The correct answer was: {ques_ans}\nYour current score is: {self.score}/{self.ques_number}\n")

    def still_has_questions(self):
        """
        returns true if there is any question left to ask
        """
        if not self.remaining_questions:
            print(f"\nQUIZ OVER!!!!!\nYour final score is: {self.score}/{self.ques_number}")
            return False
        else:
            return True

    def play_quiz(self):
        """
        steps to play quiz
        """
        while self.still_has_questions():
            ques_ans, input_ans = self.next_question()
            self.check_answer(ques_ans, input_ans)
