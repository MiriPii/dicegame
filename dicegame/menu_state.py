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
        print("")
        print("----------------")
        print(" MenuState INIT ")
        self.init = True

        # Set BackGround
        self.bg = pygame.Surface(self.display.get_size())
        self.bg = self.bg.convert()
        self.bg.fill(GREEN)

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
            print(" MenuState working normally ")
            self.init = False

        # Draw updates onto display
        pygame.display.flip()
        pygame.display.update()
