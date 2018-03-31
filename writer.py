# -*- coding: utf-8 -*-

from dictionary import Dictionary
from character import Character

class Writer:
	def __init__(self, author, chapter_number, title):
		type_of_file = '.txt'
		self.line_limit = 90
		self.file_name = 'chapter_' + str(chapter_number) + type_of_file
		self.dictionary = Dictionary()

		self.text = ''
		self.word_count = len(title.split())
		self.characters = {}

		self.text_file = open(self.file_name, 'w')
		self.head(chapter_number, title, author)
		self.footer = '[Made with Love and https://github.com/W01fw00d/chapter_writer.git]'

	def addCharacter(self, identificator, names):
		character = Character(names)
		self.characters[identificator] = character

	def addDialog(self, identificator, input_text):
		text = ' - ' + input_text + ' - ' + self.dictionary.getRandomSayVerb() + ' ' + self.characters[identificator].getRandomName() + '.'
		self.writeParagraph(text)

	def head(self, chapter_number, title, writer):
		self.text += "%s. %s" % (chapter_number, title)
		self.text += '\n'
		self.text += "by %s" % writer
		self.text += '\n'
		self.text += '\n'

	def writeParagraph(self, input_text):
		splitted_text = input_text.split()
		next_text = ''
		current_line = ''

		for word in splitted_text:
			if (len(current_line + word) <= self.line_limit):
				current_line += word + ' '
				
			else:
				next_text += current_line + '\n'
				current_line = word + ' '
			
			self.word_count += 1
			
		next_text += current_line + '\n'
			
		self.text += next_text + '\n'

	def narrate(self, new_text):
		self.writeParagraph(new_text)

	def addIntermission(self, new_text):
		formatted_text = '--- ' + self.dictionary.getRandomIntermissionAdverb() + ', ' + new_text + ' '
		sufix_decorator_multiplier = self.line_limit - len(formatted_text)
		sufix_decorator_multiplier = sufix_decorator_multiplier if (sufix_decorator_multiplier >= 0) else 0
	
		self.text += formatted_text + (sufix_decorator_multiplier * '-') + ('\n' * 2)

	def finish(self):
		self.text += self.footer
		self.text_file.write(self.text)
		self.text_file.close()
		print('"' + self.file_name + '" succesfully created')
		print('Words: ' + str(self.word_count))
