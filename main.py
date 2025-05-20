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
        self.clock = pygame.time.Clock()

    # run the screen
    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            self.screen.fill((0, 0, 0))
            pygame.display.flip()
            self.clock.tick(30)

        pygame.quit()
        sys.exit()

# call main
if __name__ == "__main__":
    app = QuizCreatorApp()
    app.run()