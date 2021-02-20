"""
Handles the main loop, error reporting, and the various other state managers
"""
import pygame
import pygame.locals as locals

from sys import exc_info #needed for error reporting
import traceback #needed for error reporting

import misc

class Game:
    def __init__(self):
        pygame.init()

        self.values = misc.ValueHolder()
        self.settings = misc.GameSettings()

        #Set up the screen
        self.screen = pygame.display.set_mode((self.settings.width, self.settings.height))
        pygame.display.set_caption("Mercenaries")

    def main_loop(self):

        while True:

            try:
                events = pygame.event.get()

                for event in events:
                    if event.type == locals.QUIT:
                        self.quit_game()
    
                pygame.display.update()

            except Exception:
                tb = exc_info()  # return error information
                print("Error found in main loop")
                print()
                print("Error type:", tb[0])
                print("Error value:", tb[1])
                l = traceback.format_tb(tb[2])
                for line in l:
                    print(line)
                self.quit_game()  # if reactor has already started, shut down the game

    def quit_game(self):
        pygame.quit()
        raise SystemExit