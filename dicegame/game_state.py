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
        print("")
        print("----------------")
        print(" GameState INIT ")
        self.init = True

        # Set BackGround
        self.bg = pygame.Surface(self.display.get_size())
        self.bg = self.bg.convert()
        self.bg.fill(PINK)

        # Screen size
        scr_w = self.bg.get_width()
        scr_h = self.bg.get_height()

        # Set fonts and menu items
        font_path = "./../fonts/"
        self.text_font = pygame.font.Font(None, 24)

        # Set instructions
        self.info = self.text_font.render("This is test screen. ESC to QUIT.",
                                        0, BLACK)
        self.inforect = self.info.get_rect()
        self.inforect.centerx = self.bg.get_rect().centerx
        self.inforect.y = scr_h-80

        self.info2 = self.text_font.render("Press SPACE-key to load next state.", 0, BLACK)
        self.info2rect = self.info2.get_rect()
        self.info2rect.centerx = self.bg.get_rect().centerx
        self.info2rect.y = scr_h-50
        self.bg.blit(self.info, self.inforect)
        self.bg.blit(self.info2, self.info2rect)

        # Draw the initial display
        self.display.blit(self.bg, (0, 0))

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
            print(" GameState working normally ")
            self.init = False

        # Draw updates onto display
        pygame.display.flip()
        pygame.display.update()
