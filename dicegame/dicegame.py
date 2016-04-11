#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: Miri Piiroinen
# DiceGame

from state_machine import StateMachine
from game_states import *

import pygame

class Game(object):
	"""	This is where the main gameloop runs.
		:param machine = Creates an instance of StateMachine."""

	def __init__(self):

		pygame.init()
		self.machine = StateMachine()

	def run(self):

		self.display = pygame.display.set_mode((800,600))
		pygame.display.set_caption('The DiceGame')
		self.clock = pygame.time.Clock()

		self.machine.load(IntroState(self.machine, self.display))

		while self.machine.isRunning():

			self.machine.nextState()
			self.machine.update()
			self.machine.draw()
			self.clock.tick(30)
