import pygame

class InputBox:
    # method initialize
    def __init__(self, x, y, w, h, label, font):
        self.rect = pygame.Rect(x, y, w, h)
        self.label = label
        self.text = ""
        self.font = font
    # method handle event
    # method draw
