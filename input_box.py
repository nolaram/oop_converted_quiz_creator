import pygame

class InputBox:
    # method initialize
    def __init__(self, x, y, w, h, label, font=None, index=0):
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
    def draw(self, screen, active_color, inactive_color, text_color):
        color = active_color if self.active else inactive_color
        pygame.draw.rect(screen, color, self.rect, 0)
        pygame.draw.rect(screen, pygame.Color("white"), self.rect, 2)

        full_text = f"{self.label}: {self.text}"
        text_surface = self.font.render(full_text, True, text_color)
        screen.blit(text_surface, (self.rect.x + 5, self.rect.y + 10))