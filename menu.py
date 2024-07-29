import pygame
from button import Button

pygame.init()

def main_menu(screen, play, options):
    while True:
        screen.fill((255, 255, 255))
        mouse_pos = pygame.mouse.get_pos()
        playButton = Button(image=pygame.image.load('assets/button.png'), x=100, y=100, text="Play")
        optionsButton = Button(image=pygame.image.load('assets/button.png'), x=100, y=300, text="Options")
        quitButton = Button(image=pygame.image.load('assets/button.png'), x=100, y=500, text="Quit")

        for button in [playButton, optionsButton, quitButton]:
            button.onHoverButton(mouse_pos)
            button.draw(screen)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if playButton.onClickButton(mouse_pos):
                    play()
                if optionsButton.onClickButton(mouse_pos):
                    options()
                if quitButton.onClickButton(mouse_pos):
                    pygame.quit()
                    exit()
        pygame.display.update()