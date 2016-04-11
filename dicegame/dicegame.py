#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: Miri Piiroinen
# DiceGame

from state_machine import StateMachine
from game_states import *

class Game(object):
	"""	This is where the main gameloop runs.
		:param machine = Creates an instance of StateMachine."""

	def __init__(self):
		self.machine = StateMachine()

		''' For Visuals (set framerate)
		self.window =
		'''

	def run(self):

		''' For Visuals
		create window
		'''

		self.machine.load(IntroState(self.machine))

		while self.machine.isRunning():

			self.machine.nextState()
			self.machine.update()
			self.machine.draw()
