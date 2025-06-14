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
        
        # timer
        start_time = time.time()
        user_answer = ""

        while user_answer not in ['a', 'b', 'c', 'd']:
            elapsed = time.time() - start_time
            remaining = self.time_limit - int(elapsed)

            if remaining <= 0:
                print("\nTime's up!")
                print(f"The correct answer was '{question.correct_answer}'.")
                return
            
            print(f"Time remaining: {remaining} seconds")
            user_answer = input("Your answer (a/b/c/d): ").lower().strip()

            if user_answer not in ['a', 'b', 'c', 'd']:
                print("Please enter a valid choice: a, b, c, or d")

        if question.is_correct(user_answer):
            print("Correct!")
            self.score += 1
        else:
            print(f"Wrong! The correct answer was '{question.correct_answer}'.")

    def show_results(self):
        print("\n=== Quiz Complete ===")
        print(f"Your Score: {self.score} out of {len(self.questions)}")

    def ask_to_retry(self):
        while True:
            choice = input("Do you want to take the quiz again? (Y/N): ").strip().lower()
            if choice == 'y':
                return True
            elif choice == 'n':
                return False
            else:
                print("Invalid input. Please enter Y or N.")
