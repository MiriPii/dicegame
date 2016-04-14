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
        self.bg.fill(BLUE)

        # Screen size
        scr_w = self.bg.get_width()
        scr_h = self.bg.get_height()

        # Menu traverse helper
        self.hl_pos = 0

        # Set fonts and menu items
        font_path = "./../fonts/"
        self.text_font = pygame.font.Font(None, 24)
        self.title_font = pygame.font.Font(font_path+"justice.ttf", 80)
        self.title_font.set_underline(True)
        self.font = pygame.font.Font(font_path+"justice.ttf", 42)
        self.font_hl = pygame.font.Font(font_path+"justice3d.ttf", 42)

        # Set Title
        self.title = self.title_font.render("DiceGame", True, BLACK)
        self.titlepos = self.title.get_rect()
        self.titlepos.centerx = self.bg.get_rect().centerx
        self.bg.blit(self.title, self.titlepos)

        # Set instructions
        self.info = self.text_font.render("Use UP and DOWN Arrows to select.",
                                        0, BLACK)
        self.inforect = self.info.get_rect()
        self.inforect.centerx = self.bg.get_rect().centerx
        self.inforect.y = scr_h-80

        self.info2 = self.text_font.render("Press Return-key to confirm your selection.", 0, BLACK)
        self.info2rect = self.info2.get_rect()
        self.info2rect.centerx = self.bg.get_rect().centerx
        self.info2rect.y = scr_h-50
        self.bg.blit(self.info, self.inforect)
        self.bg.blit(self.info2, self.info2rect)

        # Set menu elements
        self.start = self.font.render("Play Again", 0, BLACK)
        self.start_hl = self.font_hl.render("> Play Again <", 0, BLACK)
        self.quit = self.font.render("QUIT", 0, BLACK)
        self.quit_hl = self.font_hl.render("> QUIT <", 0, BLACK)
            # Set locations for the menu elements
        self.start_rect = self.start.get_rect()
        self.start_hl_rect = self.start_hl.get_rect()
        self.quit_rect = self.quit.get_rect()
        self.quit_hl_rect = self.quit_hl.get_rect()
            # Center x
        self.start_rect.centerx = self.bg.get_rect().centerx
        self.start_hl_rect.centerx = self.bg.get_rect().centerx
        self.quit_rect.centerx = self.bg.get_rect().centerx
        self.quit_hl_rect.centerx = self.bg.get_rect().centerx
            # Set y
        self.start_rect.y = scr_h//2
        self.start_hl_rect.y = scr_h//2
        self.quit_rect.y = scr_h//2+80
        self.quit_hl_rect.y = scr_h//2+80

        # Draw the initial display
        self.display.blit(self.bg, (0, 0))
        self.display.blit(self.start_hl, self.start_hl_rect)
        self.display.blit(self.quit, self.quit_rect)

    def move(self, direction):
        """ Helper function to move between menu elements. """
        if (direction == pygame.K_DOWN):
            self.hl_pos = 1
        elif (direction == pygame.K_UP):
            self.hl_pos = 0

    def update(self):

        if self.init is True:
            print(" MenuState update called ")

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                self.machine.quit()

            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_ESCAPE:
                    self.machine.quit()

                elif ((event.key == pygame.K_DOWN) or (event.key == pygame.K_UP)):
                    self.move(event.key)

                elif event.key == pygame.K_RETURN:

                    if self.hl_pos == 0:
                        self.nextSt = game_state.GameState(self.machine, self.display)
                    elif self.hl_pos == 1:
                        self.machine.quit()

    def draw(self):
        if self.init is True:
            print(" MenuState draw called ")
            print(" MenuState working normally ")
            self.init = False

        self.display.fill(BLUE)                               # Clear screen
        self.display.blit(self.bg, (0, 0))                    # Draw background

        if self.hl_pos == 1:                                # #
            self.display.blit(self.start, self.start_rect)     #
            self.display.blit(self.quit_hl, self.quit_hl_rect)    # Draw menu elements
        else:                                                 #
            self.display.blit(self.start_hl, self.start_hl_rect)  #
            self.display.blit(self.quit, self.quit_rect)     # #

        # Draw updates onto display
        pygame.display.flip()
        pygame.display.update()
