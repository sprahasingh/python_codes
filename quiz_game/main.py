from quiz_brain import QuizBrain


quiz = QuizBrain()
while not quiz.is_end():
    quiz.ask_question()
    quiz.get_answer()
    quiz.check_answer()
