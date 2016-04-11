#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: Miri Piiroinen
# DiceGame

import random
import pygame
from state import State

#Color scheme
BLACK = (0,0,0)
BLUE = (82, 101, 222)
GREEN = (82, 222, 133)
PINK = (222, 82, 171)

class IntroState(State):
	"""IntroState"""
	def __init__(self, machine, display):
		super(IntroState, self).__init__(machine,display)
		self.machine = machine
		self.display = display

		#Set BackGround
		#Set fonts and menu items

	def update(self):

		for event in pygame.event.get():

			if event.type == pygame.QUIT:
				self.machine.quit()

			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_SPACE:
					self.nextSt = GameState(self.machine, self.display)

		"""
		print("")
		print(" ---- ")
		print("Welcome to DiceGame")
		print(" ---- ")
		print("")
		print("The games rules are very simple!")
		print("You try to guess the correct sum of a two die rolls.")
		print("")
		print("If you guessed correctly you win the game.")
		print("Otherwise you lose.")
		print("")
		print("")
		print("------------")
		answer = input("Type (Y) to play the game!\nType (N) to quit the game!\n")
		while answer.lower() not in {'y','n'}:
			print("Only (Y) and (N) are accepted!")
			answer = input("Do you want to play?\n")

		if answer.lower() == 'y':
			print("")
			print("")
			self.nextSt = GameState(self.machine, self.display)
		else:
			print("Sad to see you go!")
			print("Good day to you and don't forget to smile!")
			print("")
			print("------------")
			print("Press any key to quit.")
			input()
			print("")
			self.machine.quit()
	"""

	def draw(self):

		self.display.fill(BLUE)
		# Draw updates onto display
		pygame.display.update()


class GameState(State):
	"""GameState"""

	def __init__(self, machine, display):
		super(GameState, self).__init__(machine,display)
		self.machine = machine
		self.display = display

	def update(self):

		print("I am going to roll 2 dies.")
		print("If you quess the sum of the rolls you win the game!")
		print("")
		print("------------")
		quess = input("What do you think the rolls will be in total? [2-12]\n")
		while quess not in {'2','3','4','5','6','7','8','9','10','11','12'}:
			print("Choose a number from range [2-12].")
			quess = input()
		quess = int(quess)
		Dice_1 = random.randint(1,6)
		Dice_2 = random.randint(1,6)
		sum_of_dies = Dice_1+Dice_2
		print("")
		print("------------")
		print("You quessed: {}".format(quess))
		print("*Dies are rolling and tension is growing!*")
		print("The dies rolled:")
		print("		Dice#1 : {}".format(Dice_1))
		print("		Dice#2 : {}".format(Dice_2))
		print("		___________")
		print("		   SUM : {}".format(sum_of_dies))
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

		while answer.lower() not in {'y','n'}:
			print("Only (Y) and (N) are accepted!")
			answer= input()

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