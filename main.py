import pygame
from menu import main_menu
from game import mainGame

pygame.init()
WIDTH, HEIGHT = 700, 700
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tic Tac Toe")

def options():
    print("Options")
