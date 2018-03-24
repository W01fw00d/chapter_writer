# -*- coding: utf-8 -*-

class Writer:
	def __init__(self, writer, chapter_number, title):
		type_of_file = '.txt'
	
		self.line_limit = 80
		self.text = ''
		self.text_file = open('chapter_' + str(chapter_number) + type_of_file, 'w')
		self.head(chapter_number, title, writer)
		self.footer = '[Made with Love and https://github.com/W01fw00d/chapter_writer.git]'
		
	def head(self, chapter_number, title, writer):
		self.text += "%s. %s" % (chapter_number, title)
		self.text += '\n'
		self.text += "by %s" % writer
		self.text += '\n'
		self.text += '\n'
		
	def write(self, new_text):
		new_text += '.'
		lines = [new_text[i:i+self.line_limit] for i in range(0, len(new_text), self.line_limit)]
		for line in lines:
			self.text += line + '\n'
			
		self.text += '\n'
		
	def narrate(self, new_text):
		self.write(new_text)
		
	def end(self):
		self.text += self.footer
		self.text_file.write(self.text)
		self.text_file.close()
