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

                    if line.startswith("Question: "):
                        if current_data:
                            questions.append(Question(
                                current_data['question_text'],
                                current_data['option_a'],
                                current_data['option_b'],
                                current_data['option_c'],
                                current_data['option_d'],
                                current_data['correct_answer']
                            ))
                            current_data = {}

                        current_data["question_text"] = line[len("Question: "):]

                    elif line.startswith("a) "):
                        current_data["option_a"] = line[len("a) "):]
                    
                    elif line.startswith("b) "):
                        current_data["option_b"] = line[len("b) "):]
                    
                    elif line.startswith("c) "):
                        current_data["option_c"] = line[len("c) "):]
                    
                    elif line.startswith("d) "):
                        current_data["option_d"] = line[len("d) "):]

                    elif line.startswith("Correct Answer: "):
                        current_data["correct_answer"] = line[len("Correct Answer: "):]
                        
    # return questions read