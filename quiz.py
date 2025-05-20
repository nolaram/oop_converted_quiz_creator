# import all things needed
import time
import sys

# class
class Quiz:
    # construct method
    def __init__(self, questions, time_limit=30):
        # question
        self.questions = questions
        # time limit
        self.time_limit = time_limit
        # score
        self.score = 0

    # main function to start the program
    def start(self):
        # loop
        for i, question in enumerate(self.questions, start=1):
            self.ask_question(i, question)
        # display results
        self.show_results()
        # ask to retry
        if self.ask_to_retry():
            self.score = 0
            self.start()
        else:
            print("Thank you for playing!")
            sys.exit()
    # handle display
    def ask_question(self, number, question):
        # show the question
        print(f"\nQuestion {number}: {question.question_text}")
        for key in ['a', 'b', 'c', 'd']:
            print(f"  {key}) {question.options[key]}")
        # display options
        # timer