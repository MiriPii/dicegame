#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: Miri Piiroinen
# DiceGame

import random
import pygame
from state import State

# Color scheme
BLACK = (0, 0, 0)
BLUE = (82, 101, 222)
GREEN = (82, 222, 133)
PINK = (222, 82, 171)


class IntroState(State):
    """IntroState"""
    def __init__(self, machine, display):
        super(IntroState, self).__init__(machine, display)
        self.machine = machine
        self.display = display

        # Set BackGround
        self.bg = pygame.Surface(self.display.get_size())
        self.bg = self.bg.convert()
        self.bg.fill(BLUE)

        # Screen size
        scr_w = self.bg.get_width()
        scr_h = self.bg.get_height()

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
        self.info = self.text_font.render("Use UP and DOWN to move.",
                                        0, BLACK)
        self.inforect = self.info.get_rect()
        self.inforect.centerx = self.bg.get_rect().centerx
        self.inforect.y = self.titlepos.y+80

        self.info2 = self.text_font.render("Press Return-key to confirm selection.", 0, BLACK)
        self.info2rect = self.info2.get_rect()
        self.info2rect.centerx = self.bg.get_rect().centerx
        self.info2rect.y = self.inforect.y+30
        self.bg.blit(self.info, self.inforect)
        self.bg.blit(self.info2, self.info2rect)

        # Set temporary bg, so menuitems can be changed
        self.tempbg = self.bg

        # Set items
        self.start = self.font.render("Start Game", 0, BLACK)
        self.start_hl = self.font_hl.render("Start Game", 0, BLACK)
        self.quit = self.font.render("QUIT", 0, BLACK)
        self.quit_hl = self.font_hl.render("QUIT", 0, BLACK)

        # Set locations for the menu items
        self.startrect = self.start.get_rect()
        self.quitrect = self.quit.get_rect()
        # Center x
        self.startrect.centerx = self.bg.get_rect().centerx
        self.quitrect.centerx = self.bg.get_rect().centerx
        # Set y
        self.startrect.y = scr_h//2
        self.quitrect.y = scr_h//2+80
        # Draw the menu items to temp bg
        self.tempbg.blit(self.start_hl, self.startrect)
        self.tempbg.blit(self.quit, self.quitrect)

        # Draw the initial display
        self.display.blit(self.tempbg, (0, 0))
        pygame.display.flip()

        # Menu traverse helper
        self.hl_pos = 0

    def move(self, direction):

        self.tempbg = self.bg
        if ((direction == pygame.K_DOWN) and (self.hl_pos != 1)):
            self.hl_pos = 1
            self.tempbg.blit(self.start, self.startrect)
            self.tempbg.blit(self.quit_hl, self.quitrect)
        if ((direction == pygame.K_UP) and (self.hl_pos != 0)):
            self.hl_pos = 0
            self.tempbg.blit(self.start_hl, self.startrect)
            self.tempbg.blit(self.quit, self.quitrect)

        print(self.hl_pos)


    def update(self):

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
                        self.nextST = GameState(self.machine, self.display)
                    elif self.hl_pos == 1:
                        self.machine.quit()

    def draw(self):

        self.display.fill(BLUE)
        self.display.blit(self.tempbg, (0, 0))

        # Draw updates onto display
        pygame.display.flip()
        pygame.display.update()


class GameState(State):
    """GameState"""

    def __init__(self, machine, display):
        super(GameState, self).__init__(machine, display)
        self.machine = machine
        self.display = display
        print(" GameState init ")

    def update(self):

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
            self.nextSt = MenuState(self.machine, self.display)

    def draw(self):

        self.display.fill(PINK)
        # Draw updates onto display
        pygame.display.update()


class MenuState(State):
    """MenuState"""

    def __init__(self, machine, display):
        super(MenuState, self).__init__(machine, display)
        self.machine = machine
        self.display = display

    def update(self):
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
            self.nextSt = GameState(self.machine, self.display)
        else:
            print("")
            print("------------")
            print("You are leaving already?")
            print("I hope to see you soon! Have a great day!")
            print("And don't forget to smile!")
            input("Press any key to close the game.")
            self.machine.quit()

    def draw(self):

        self.display.fill(GREEN)
        # Draw updates onto display
        pygame.display.update()
