class Question:
    # constructor method
    def __init__(self, question_text, option_a, option_b, option_c, option_d, correct_answer):
        self.question_text = question_text
        # parameters
        self.options = {
            'a': option_a,
            'b': option_b,
            'c': option_c,
            'd': option_d
        }
        self.correct_answer = correct_answer.lower()

    # check if correct
    def is_correct(self, user_answer):
        return user_answer == self.correct_answer