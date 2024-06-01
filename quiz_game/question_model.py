from data import question_data


class Question:
    def __init__(self, q_text, q_answer):
        self.text = q_text
        self.answer = q_answer


qna_list = [Question(data["text"], data["answer"]) for data in question_data]


# question_bank = []
# for data in question_data:
#     question_bank.append(Question(data["text"], data["answer"]))
#
# new_question_bank = []
#
#
# def get_question():
#     if quiz.is_question_asked():
#         for ques in question_bank:
#             if quiz.question_detail != ques:
#                 new_question_bank.append(question_bank)
#     return new_question_bank
#
#
# question_bank = get_question()
