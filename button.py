import pygame

pygame.init()
main_font = pygame.font.SysFont("comic sans ms", 50)

class Button():
    def __init__(self, image, x, y, text):
        self.image = image
        self.x = x
        self.y = y
        #making a rect object for the button
        self.rect = self.image.get_rect(center=(x, y))
        self.text = text
        self.text_surface = main_font.render(text, True, (204, 41, 68))
        self.text_rect = self.text_surface.get_rect(center=(x, y))
    
    def draw(self, screen):
        screen.blit(self.image, self.rect)
        screen.blit(self.text_surface, self.text_rect)
    
    def onClickButton(self, position):
        if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
            return True
    def onHoverButton(self, position):
        if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
            self.image = pygame.image.load('assets/buttonhover.png')
            self.text_surface = main_font.render(self.text, True, (231, 214, 207))
        else:
            self.text_surface = main_font.render(self.text, True, (204, 41, 68))
            self.image = pygame.image.load('assets/button.png')