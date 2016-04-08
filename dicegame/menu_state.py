#!/usr/bin/env python
# -*- coding: utf-8 -*-

from state_manager import State
from game_state import GameState

class MenuState(State):
	"""This state is where the actual game happens."""

	def __init__(self):
		print("MenuState Init")
		print("---")
		print("Controls:")
		print("Y : Start a new game.")
		print("N : Quit the game.")

	def pause(self):
		print("MenuState Pause")

	def resume(self):
		print("MenuState Resume")

	def update(self):
		answer = input("What do you want to do: ")
		if (answer.lower() = 'y' or answer.lower() = 'yes'):
			self.load(GameState)
			break

		elif (answer.lower() = 'n' or answer.lower() = 'no'):
			self.machine.quit()
			break
		else:
			print("Unknown command.")
			break

	def draw(self):
		pass
