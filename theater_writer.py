# -*- coding: utf-8 -*-

from writer import Writer
from dictionary import Dictionary
from character import Character

class TheaterWriter(Writer):

	def addCharacter(self, code, names):
		character = Character(code)
		self.characters[code] = character

	def addDialog(self, code, input_text):
		text = code.upper() + ': ' + input_text + '.'
		self.writeParagraph(text)
