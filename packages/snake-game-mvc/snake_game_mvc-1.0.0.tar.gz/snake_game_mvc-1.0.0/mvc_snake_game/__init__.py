__all__ = ["mvc_snake_game"]
from os import environ
environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'

import pygame
from mvc_snake_game.model import Game
from mvc_snake_game.view import Window

def main():
    game = Game()
    window = Window()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        if window.menu == True:
            game.menu(window)
        
        else:
            if window.gameover == False and window.menu == False and window.select_diff == True:
                game.select_diff(window, game)

            if window.gameover == True and window.menu == False and window.select_diff == False:
                game.score_menu(window)
                    
            if window.gameover == False and window.menu == False and window.select_diff == False:
                game.game(window)

main()