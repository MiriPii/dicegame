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
        self.dice1_pos = (self.bg.get_rect().centerx-80, self.bg.get_rect().centery+100)
        self.dice2_pos = (self.bg.get_rect().centerx+80, self.bg.get_rect().centery+100)
        self.rollcount = 0

        # Set fonts and menu items
        font_path = "./../fonts/"
        self.text_font = pygame.font.Font(None, 24)
        self.quess_font = pygame.font.Font(None, 38)

        # Set possible quesses
        self.quesses = []
        self.quessnum = 0
        for i in range(11):
            self.quesses.append(self.quess_font.render("{}".format(i+2),
                                        0, BLACK))

        # Set instructions and static bg

        rules = []
        rulesrect = []
        rules.append(self.text_font.render("INSTRUCTIONS:",
                                        0, BLACK))
        rules.append(self.text_font.render("Your object is to quess the total of two dice rolls.",
                                        0, BLACK))
        rules.append(self.text_font.render("Input your quess to the box [2-12] and confirm with Return-key.",
                                        0, BLACK))
        for rule in rules:
            rulesrect.append(rule.get_rect())
            counter = len(rulesrect)-1
            rulesrect[counter].centerx = self.bg.get_rect().centerx
            rulesrect[counter].y = scr_h-80+(counter*30)

        for i in range(3):
            self.bg.blit(rules[i], rulesrect[i])
        # Static line reading 'Your quess: ___'
        your_quess = self.quess_font.render("Your quess: ___", 0, BLACK)
        your_quessrect = your_quess.get_rect()
        your_quessrect.centerx = self.bg.get_rect().centerx+30
        your_quessrect.y = 200
        self.bg.blit(your_quess, your_quessrect)

        # Draw the initial display
        self.display.blit(self.bg, (0, 0))
        self.display.blit(self.quesses[0], (500, 200) )

        # Create Dice phases
        self.dice_sheet = pygame.image.load("../img/dice_cropped.png")
        self.dice = []
        self.dicecrop = pygame.Surface((53, 54))
        for i in range(6):
            self.dicecrop = pygame.Surface((53, 54))
            self.dice.append(self.dicecrop)
            self.dice[i].blit(self.dice_sheet, (0, 0), (i*53, 0, 53, 54))
        self.counter = 0

    def update(self):
        if self.init is True:
            print(" GameState update called ")

        if self.phases[self.gamephase] == "roll":
            if self.rollcount < 20:
                self.dice1_val = random.randint(1, 6)
                self.dice2_val = random.randint(1, 6)
                self.rollcount+=1
            else:
                self.dice_sum = self.dice1_val+self.dice2_val
                self.gamephase=2

        if self.phases[self.gamephase] == "result":
            if self.dice_sum == self.quessnum+2:
                print("Congratz! You win! You quessed: {}".format(self.quessnum+2))
                print("                The answer was: {}".format(self.dice_sum))
            else:
                print("Too Bad! You lost! You quessed: {}".format(self.quessnum+2))
                print("                The answer was: {}".format(self.dice_sum))

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
                        self.display.fill(PINK)
                        self.display.blit(self.bg, (0, 0))
                        self.display.blit(self.quesses[self.quessnum], (500, 200))

                    elif event.key == pygame.K_DOWN:
                        if self.quessnum <= 0:
                            self.quessnum = 0
                        else:
                            self.quessnum -= 1
                        self.display.fill(PINK)
                        self.display.blit(self.bg, (0, 0))
                        self.display.blit(self.quesses[self.quessnum], (500, 200))

                    elif event.key == pygame.K_RETURN:
                        self.gamephase = 1
            elif self.phases[self.gamephase] == "result":
                self.nextSt = menu_state.MenuState(self.machine, self.display)

    def draw(self):
        if self.init is True:
            print(" GameState draw called ")
            print(" GameState working normally ")
            self.init = False

        if self.phases[self.gamephase] == "roll":
            self.display.blit(self.dice[self.dice1_val-1], self.dice1_pos)
            self.display.blit(self.dice[self.dice2_val-1], self.dice2_pos)
            time.sleep(0.2)

        # Draw updates onto display
        pygame.display.flip()
        pygame.display.update()
