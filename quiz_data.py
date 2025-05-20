class QuizDataWriter:
    # method constructor
    def __init__(self, filename):    
        # file name
        self.filename = filename

    # save method
    def save(self, inputs):
        with open(self.filename, 'a') as file:
            file.write(f'Question: {inputs[0]}\n')
            file.write(f'a) {inputs[1]}\n')
            file.write(f'b) {inputs[2]}\n')
            file.write(f'c) {inputs[3]}\n')
            file.write(f'd) {inputs[4]}\n')
            file.write(f'Correct Answer: {inputs[5].lower()}\n')
            file.write('-' * 40 + '\n')