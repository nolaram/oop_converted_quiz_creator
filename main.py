# import all things needed
import pygame
import sys
from input_box import InputBox
from quiz_data import QuizDataWriter

class QuizCreatorApp:
    # constructor method
    def __init__(self):
        # screen
        pygame.init()
        self.WIDTH, self.HEIGHT = 800, 600
        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        pygame.display.set_caption('Quiz Creator')

        self.font = pygame.font.SysFont("comic sans ms", 28)
        self.confirm_font = pygame.font.SysFont("comic sans ms", 32)
        self.title_font = pygame.font.SysFont("arial", 50, bold=True)

        # Colors
        self.COLOR_BACKGROUND = pygame.Color("#1e1e1e")
        self.COLOR_TEXT = pygame.Color("#ffffff")
        self.COLOR_ACTIVE = pygame.Color("#00bfff")
        self.COLOR_INACTIVE = pygame.Color("#3a3f55")
        self.COLOR_CONFIRM = pygame.Color("lightgreen")

        self.clock = pygame.time.Clock()
        self.running = True

        # Labels and input boxes
        self.labels = [
            "Questions", "Option A", "Option B",
            "Option C", "Option D", "Correct Answer (a/b/c/d)"
        ]
        self.inputs = [""] * len(self.labels)
        self.input_boxes = [
            InputBox(50, 50 + i * 60, 700, 40, self.labels[i], self.font, i)
            for i in range(len(self.labels))
        ]

        self.active_index = 0
        self.state = "input"
        self.writer = QuizDataWriter("quiz_data.txt")

    # run the screen
    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

                elif event.type == pygame.KEYDOWN:
                    if self.state == "input":
                        if event.key == pygame.K_TAB:
                            self.active_index = (self.active_index + 1) % len(self.input_boxes)
                        elif event.key == pygame.K_RETURN:
                            inputs = [box.text for box in self.input_boxes]
                            if all(inputs) and inputs[5].lower() in ["a", "b", "c", "d"]:
                                self.writer.save(inputs)
                                for box in self.input_boxes:
                                    box.text = ""
                                self.state = "confirm"
                            else:
                                print("Fill all fields properly and ensure correct answer is a/b/c/d.")
                        else:
                            self.input_boxes[self.active_index].handle_event(event)

                    elif self.state == "confirm":
                        if event.key == pygame.K_y:
                            for box in self.input_boxes:
                                box.text = ""
                            self.active_index = 0
                            self.state = "input"
                        elif event.key == pygame.K_n:
                            running = False

            self.screen.fill(self.COLOR_BACKGROUND)

            for index, box in enumerate(self.input_boxes):
                box.active = (index == self.active_index)
                box.draw(self.screen, self.COLOR_ACTIVE, self.COLOR_INACTIVE, self.COLOR_TEXT)

            pygame.display.flip()
            self.clock.tick(30)

        pygame.quit()
        sys.exit()

# call main
if __name__ == "__main__":
    app = QuizCreatorApp()
    app.run()