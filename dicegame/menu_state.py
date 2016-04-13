#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: Miri Piiroinen
# DiceGame

import pygame
import game_state
from state import State

# Color scheme
BLACK = (0, 0, 0)
BLUE = (82, 101, 222)
GREEN = (82, 222, 133)
PINK = (222, 82, 171)


class MenuState(State):
    """MenuState"""

    def __init__(self, machine, display):
        super(MenuState, self).__init__(machine, display)
        self.machine = machine
        self.display = display

        # Debug helpers
        print(" MenuState INIT ")
        self.init = True

    def update(self):

        if self.init is True:
            print(" MenuState update called ")

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                self.machine.quit()

            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_ESCAPE:
                    self.machine.quit()

                elif event.key == pygame.K_SPACE:
                    self.nextSt = game_state.GameState(self.machine, self.display)
        '''
        print("")
        print("------------")
        print("Would you like to play a new game or quit?")
        print("Choose 'Y' to start a new game.")
        print("Choose 'N' to quit the game.")
        answer = input()

        while answer.lower() not in {'y', 'n'}:
            print("Only (Y) and (N) are accepted!")
            answer = input()

        if answer.lower() == 'y':
            print("")
            print("------------")
            print("Great! I wish you the best luck!")
            input("Press any key to start the game.")
            self.nextSt = game_state.GameState(self.machine, self.display)
        else:
            print("")
            print("------------")
            print("You are leaving already?")
            print("I hope to see you soon! Have a great day!")
            print("And don't forget to smile!")
            input("Press any key to close the game.")
            self.machine.quit()
        '''

    def draw(self):
        if self.init is True:
            print(" MenuState draw called ")
            self.init = False

        self.display.fill(GREEN)
        # Draw updates onto display
        pygame.display.update()
