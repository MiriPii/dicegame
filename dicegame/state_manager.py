#!/usr/bin/env python
# -*- coding: utf-8 -*-

class State(object):
	"""The SuperClass for defining GameStates"""

	def __init__(self):
		pass

	def pause(self):
		pass

	def resume(self):
		pass

	def update(self):
		pass

	def draw(self):
		pass

class StateMachine(object):
	"""Manages changing from state to other state.
	Closing the current state, and exiting altogether."""

	def __init__(self):

		self.resume = False
		self.running = False
		self.states = []

	def load(self, state):

		self.running = True
		self.states.append(state)

	def nextState(self):

		if (self.resume):
			if len(self.states) != 0:
				self.states.pop()

			if len(self.states) != 0:
				self.states[len(states)-1].resume()

			self.resume = False

		# Avoid running out of states unnoticed
		if len(self.states):
			temp = self.states[len(self.states)-1].next()

			# Change if the resume state exists
			if temp:
				#Replace the current state
				if temp.isReplacing():
					self.states.pop()
				# Pause the current state
				else:
					self.states[len(states)-1].pause()

				self.states.append(temp)

	def lastState(self):
		self.resume = True

	def update(self, dt):
		self.states[len(states)-1].update(dt)

	def draw(self):
		self.states[len(states)-1].draw()

	def quit(self):
		self.running = False

	def build(self, machine, replace = True):
		pass #FIXME