# -*- coding: utf-8 -*-

class ChapterWriter:
	def __init__(self, text_file_name, writer, chapter_number, title):
		self.line_limit = 80
		self.text = ''
		self.text_file = open(text_file_name, 'w')
		self.head(chapter_number, title, writer)
		
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
		self.text += '[Made with Love and https://github.com/W01fw00d/chapter_writer.git]'
		self.text_file.write(self.text)
		self.text_file.close()


file_name = 'chapter.txt'	
writer_name = 'Gabo'
chapter_number = 6
chapter_title = 'Patrones'

write = ChapterWriter(file_name, writer_name, chapter_number, chapter_title)		

write.narrate('Era un nuevo día en la bella Barceloneta. Hacia mucho viente, y las banderas independendistas parecían a punto de reclamar su propia independencia respecto a los balcones que las sujetaban')
write.narrate('Poco sospechaba Úrsula que aquel seria el día de su propia muerte')

write.end()


