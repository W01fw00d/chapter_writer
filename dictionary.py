# -*- coding: utf-8 -*-

import random

class Dictionary:
	def __init__(self):
		self.say_verbs = ['dijo', 'musitó', 'farfulló', 'proclamó', 'parloteó', 'exclamó', 'susurró', 'anunció', 'pronunció', 'compartió', 'comunicó', 'informó']
		self.intermission_adverbs = ['Mientras tanto', 'Al mismo tiempo', 'A la vez', 'Mientras ocurría todo eso', 'En paralelo', 'Paralelamente', 'Simultáneamente']

	def getRandomSayVerb(self):
		return random.choice(self.say_verbs)

	def getRandomIntermissionAdverb(self):
		return random.choice(self.intermission_adverbs)
