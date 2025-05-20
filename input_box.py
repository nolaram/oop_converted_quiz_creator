import pygame

class InputBox:
    # method initialize
    def __init__(self, x, y, w, h, label, font, index):
        self.rect = pygame.Rect(x, y, w, h)
        self.label = label
        self.text = ""
        self.font = font
        self.index = index
        self.active = False

    # method handle event
    def handle_event(self, event):
        if event.type == pygame.KEYDOWN and self.active:
            if event.key == pygame.K_BACKSPACE:
                self.text = self.text[:-1]
            else:
                self.text += event.unicode

    # method draw
