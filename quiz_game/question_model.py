from data import question_data


class Question:
    def __init__(self, q_text, q_answer):
        self.text = q_text
        self.answer = q_answer


qna_list = [Question(data["text"], data["answer"]) for data in question_data]
