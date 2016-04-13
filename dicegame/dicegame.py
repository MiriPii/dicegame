#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: Miri Piiroinen
# DiceGame

from state_machine import StateMachine
import intro_state

import pygame


class Game(object):
    """ This is where the main gameloop runs.
        :param machine = Creates an instance of StateMachine."""

    def __init__(self):

        pygame.init()
        self.machine = StateMachine()
        self.display_w = 800
        self.display_h = 600

    def run(self):

        self.display = pygame.display.set_mode((self.display_w,self.display_h))
        pygame.display.set_caption('The DiceGame')
        self.clock = pygame.time.Clock()

        self.machine.load(intro_state.IntroState(self.machine, self.display))

        while self.machine.isRunning():

            self.machine.nextState()
            self.machine.update()
            self.machine.draw()
            self.clock.tick(30)
            # Debug
            if (len(self.machine.states) > 1):
                print("Machinestates: '{}'".format(self.machine.states))

        print("")
        print("----------------")
        print("DiceGame succesfully terminated.")
        print("Now clearing pygame.")
        print("")
        pygame.quit()
