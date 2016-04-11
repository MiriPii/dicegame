#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: Miri Piiroinen
# DiceGame

class State(object):
	"""The SuperClass for States.

		:func update = Step forward in time and update modified parameters
		:func draw = Draw the visuals into the specified window."""

	def __init__(self, machine, window):

		self.machine = machine
		self.window = window
		self.nextSt = None

	def update(self):
		pass

	def draw(self):
		pass

	def getNext(self):
		return self.nextSt