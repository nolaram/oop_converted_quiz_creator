# import the question file
from question import Question
# class
class QuizLoader:
    @staticmethod
    # load the questions
    def load_questions_from_file(file_path):
        questions = []

        try:
            # open the file
            with open(file_path, 'r', encoding='utf-8') as file:
                current_data = {}

                # loop through each line
                for line in file:
                    line = line.strip()
                    
    # return questions read