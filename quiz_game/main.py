from quiz_brain import QuizBrain
from question_model import Question
from data import question_data

qna_list = [Question(data["text"], data["answer"]) for data in question_data]
quiz = QuizBrain(qna_list)
quiz.play_quiz()
