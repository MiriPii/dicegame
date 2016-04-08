#!/usr/bin/env python
# -*- coding: utf-8 -*-

from state_manager import State
from menu_state import MenuState

class GameState(State):
	"""This state is where the actual game happens."""

	def __init__(self):
		print("GameState Init")
		print("---")

	def pause(self):
		print("GameState Pause")

	def resume(self):
		print("GameState Resume")

	def update(self):
		print("Dies rolling and atmosphere is so tense.")
		print("Game ended and results showing.")
		print("Returning back to menu.")

		self.load(MenuState)

	def draw(self):
		pass