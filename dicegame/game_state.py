#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: Miri Piiroinen
# DiceGame

import random
import pygame
import menu_state
from state import State

# Color scheme
BLACK = (0, 0, 0)
BLUE = (82, 101, 222)
GREEN = (82, 222, 133)
PINK = (222, 82, 171)


class GameState(State):
    """GameState"""

    def __init__(self, machine, display):
        super(GameState, self).__init__(machine, display)
        self.machine = machine
        self.display = display

        # Debug helpers
        print(" GameState INIT ")
        self.init = True

    def update(self):
        if self.init is True:
            print(" GameState update called ")

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                self.machine.quit()

            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_ESCAPE:
                    self.machine.quit()

                elif event.key == pygame.K_SPACE:
                    self.nextSt = menu_state.MenuState(self.machine, self.display)
        '''
        print("I am going to roll 2 dies.")
        print("If you quess the sum of the rolls you win the game!")
        print("")
        print("------------")
        quess = input("What do you think the rolls will be in total? [2-12]\n")
        while quess not in {'2', '3', '4', '5', '6',
                            '7', '8', '9', '10', '11', '12'}:
            print("Choose a number from range [2-12].")
            quess = input()
        quess = int(quess)
        Dice_1 = random.randint(1, 6)
        Dice_2 = random.randint(1, 6)
        sum_of_dies = Dice_1+Dice_2
        print("")
        print("------------")
        print("You quessed: {}".format(quess))
        print("*Dies are rolling and tension is growing!*")
        print("The dies rolled:")
        print("     Dice#1 : {}".format(Dice_1))
        print("     Dice#2 : {}".format(Dice_2))
        print("     ___________")
        print("        SUM : {}".format(sum_of_dies))
        print("")
        if sum_of_dies == quess:
            print("")
            print("------------")
            print("AWESOME! You guessed the sum correctly!")
            game_finished = True
        else:
            print("")
            print("------------")
            print("OH! Too bad. Your quess was wrong.")
            print("Better luck next time!")
            game_finished = True

        if game_finished:
            self.nextSt = menu_state.MenuState(self.machine, self.display)
        '''

    def draw(self):
        if self.init is True:
            print(" GameState draw called ")
            self.init = False

        self.display.fill(PINK)
        # Draw updates onto display
        pygame.display.update()
