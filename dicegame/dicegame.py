#!/usr/bin/env python
# -*- coding: utf-8 -*-

from state_manager import StateMachine
from menu_state import MenuState


class Game(object):
	"""Inits the StateMachine.
	This is where the main gameloop runs."""

	def __init__(self):
		self.machine = StateMachine()

		''' For Visuals (set framerate)
		self.window =
		'''

	def run(self):

		''' For Visuals
		create window
		'''

		self.machine.load(MenuState)

		while len(self.machine.running):

			self.machine.nextState()
			self.machine.update( dt )
			self.machine.draw()
