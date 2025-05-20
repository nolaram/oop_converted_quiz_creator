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
# call main
