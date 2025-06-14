# import all things needed
import sys
from quiz_loader import QuizLoader
from quiz import Quiz

# call main
if __name__ == "__main__":
    # read file
    file_name = "quiz_data.txt"
    questions = QuizLoader.load_questions_from_file(file_name)

    # if no read file
    if not questions:
        print("No questions loaded. Exiting.")
        # exit
        sys.exit()

    # start quiz
    quiz = Quiz(questions)
    quiz.start()