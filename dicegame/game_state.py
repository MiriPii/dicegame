#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: Miri Piiroinen
# DiceGame

import random
import pygame
import menu_state
import time
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

        # Variables
        scr_w = self.bg.get_width()     # Screen width
        scr_h = self.bg.get_height()    # Screen height
        self.phases = ["quess" , "roll", "result"]
        self.gamephase = 0
        self.dice_sum = 0
        self.dice1_val = 0
        self.dice2_val = 0
        self.rollcount = 0

        # Set fonts and menu items
        font_path = "./../fonts/"
        self.text_font = pygame.font.Font(None, 24)
        self.quess_font = pygame.font.Font(None, 38)
        self.title_font = pygame.font.Font(font_path+"justice.ttf", 80)
        self.title_font.set_underline(True)

        # Set Title
        self.title = self.title_font.render("DiceGame", True, BLACK)
        self.titlepos = self.title.get_rect()
        self.titlepos.centerx = self.bg.get_rect().centerx
        self.bg.blit(self.title, self.titlepos)

        # Set possible quesses
        self.quesses = []
        self.quessnum = 0
        for i in range(11):
            self.quesses.append(self.quess_font.render("{}".format(i+2),
                                        0, BLACK))

        # Set instructions and static bg
        self.rules = []
        self.rulespos = []
        self.rules.append(self.text_font.render("INSTRUCTIONS:",
                                        0, BLACK))
        self.rules.append(self.text_font.render("Your object is to quess the total of two dice rolls.",
                                        0, BLACK))
        self.rules.append(self.text_font.render("Input your quess to the box [2-12] and confirm with Return-key.",
                                        0, BLACK))
        for rule in self.rules:
            self.rulespos.append(rule.get_rect())
            counter = len(self.rulespos)-1
            self.rulespos[counter].centerx = self.bg.get_rect().centerx
            self.rulespos[counter].y = scr_h-80+(counter*30)

        # Static line reading 'Your quess: ___'
        your_quess = self.quess_font.render("Your quess: ___", 0, BLACK)
        self.your_quesspos = your_quess.get_rect()
        self.your_quesspos.centerx = self.bg.get_rect().centerx+30
        self.your_quesspos.y = 150
        self.bg.blit(your_quess, self.your_quesspos)

        # Line for dice sum ('Result: ')
        self.result_line = self.quess_font.render("Result: ", True, BLACK)
        self.result_linepos = self.result_line.get_rect()
        self.result_linepos.centerx = self.your_quesspos.centerx
        self.result_linepos.y = self.your_quesspos.y+200

        # Result notifications
        self.result_win = self.quess_font.render("Congratulations! You answered correctly!", True, BLACK)
        self.result_lose = self.quess_font.render("Too bad! Your quess was wrong!", True, BLACK)
        self.result_help = self.text_font.render("Press any key to continue.", True, BLACK)
            # Result text positions
        self.result_win_pos = self.result_win.get_rect()
        self.result_lose_pos = self.result_lose.get_rect()
        self.result_help_pos = self.result_help.get_rect()
        self.result_win_pos.centerx = self.bg.get_rect().centerx
        self.result_lose_pos.centerx = self.bg.get_rect().centerx
        self.result_help_pos.centerx = self.bg.get_rect().centerx
        self.result_win_pos.y = scr_h-80
        self.result_lose_pos.y = scr_h-80
        self.result_help_pos.y = scr_h-80+30

        # Create Dice phases
        self.dice_sheet = pygame.image.load("../img/dice_cropped.png")
        self.dice = []
        self.dicecrop = pygame.Surface((53, 54))
        for i in range(6):
            self.dicecrop = pygame.Surface((53, 54))
            self.dice.append(self.dicecrop)
            self.dice[i].blit(self.dice_sheet, (0, 0), (i*53, 0, 53, 54))
        self.counter = 0
        self.dice1_pos = (self.bg.get_rect().centerx-80, self.your_quesspos.y+100)
        self.dice2_pos = (self.bg.get_rect().centerx+80, self.your_quesspos.y+100)

        # Draw the initial display
        self.display.blit(self.bg, (0, 0))
        self.display.blit(self.quesses[0], (500, self.your_quesspos.y) )
        for i in range(3):
            self.display.blit(self.rules[i], self.rulespos[i])

    def update(self):
        if self.init is True:
            print(" GameState update called ")

        if self.phases[self.gamephase] == "roll":
            if self.rollcount < 10:
                self.dice1_val = random.randint(1, 6)
                self.dice2_val = random.randint(1, 6)
                self.rollcount+=1
            else:
                self.dice_sum = self.dice1_val+self.dice2_val
                self.gamephase=2

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                self.machine.quit()

            if self.phases[self.gamephase] == "quess":

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        if self.quessnum >= 10:
                            self.quessnum = 10
                        else:
                            self.quessnum += 1

                    elif event.key == pygame.K_DOWN:
                        if self.quessnum <= 0:
                            self.quessnum = 0
                        else:
                            self.quessnum -= 1

                    elif event.key == pygame.K_RETURN:
                        self.gamephase = 1
            elif self.phases[self.gamephase] == "result":
                self.nextSt = menu_state.MenuState(self.machine, self.display)

    def draw(self):
        # Debugging helpers
        if self.init is True:
            print(" GameState draw called ")
            print(" GameState working normally ")
            self.init = False

        self.display.fill(PINK)
        self.display.blit(self.bg, (0, 0))
        self.display.blit(self.quesses[self.quessnum], (500, self.your_quesspos.y))

        if self.phases[self.gamephase] == "quess":
            for i in range(3):
                self.display.blit(self.rules[i], self.rulespos[i])

        elif self.phases[self.gamephase] == "roll":
            for i in range(3):
                self.display.blit(self.rules[i], self.rulespos[i])

            self.display.blit(self.dice[self.dice1_val-1], self.dice1_pos)
            self.display.blit(self.dice[self.dice2_val-1], self.dice2_pos)
            time.sleep(0.2)

        elif self.phases[self.gamephase] == "result":
            self.display.blit(self.quesses[self.quessnum], (500, self.your_quesspos.y))
            self.display.blit(self.dice[self.dice1_val-1], self.dice1_pos)
            self.display.blit(self.dice[self.dice2_val-1], self.dice2_pos)
            self.display.blit(self.result_line, self.result_linepos)
            self.display.blit(self.quesses[self.dice_sum-2], (500, self.result_linepos.y))
            self.display.blit(self.result_help, self.result_help_pos)

            if self.dice_sum == self.quessnum+2:
                self.display.blit(self.result_win, self.result_win_pos)
            else:
                self.display.blit(self.result_lose, self.result_lose_pos)

        # Draw updates onto display
        pygame.display.flip()
        pygame.display.update()
