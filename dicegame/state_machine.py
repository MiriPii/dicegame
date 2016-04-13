#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: Miri Piiroinen
# DiceGame


class StateMachine:

    def __init__(self):
        self.running = False
        self.states = []

    def load(self, state):

        self.running = True
        self.states.append(state)

    def isRunning(self):
        return self.running

    def quit(self):
        self.running = False

    def nextState(self):

        if len(self.states) != 0:

            temp = self.states[len(self.states)-1].getNext()

            if (temp is not None):

                self.states.pop()
                self.states.append(temp)

    def update(self):
        # Allows the state to update the game
        self.states[len(self.states)-1].update()

    def draw(self):
        # Allows the state to draw to the active window
        self.states[len(self.states)-1].draw()
