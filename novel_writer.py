# -*- coding: utf-8 -*-

from writer import Writer
from dictionary import Dictionary
from character import Character

class NovelWriter(Writer):
    def addCharacter(self, code, names):
        character = Character(code, names)
        self.characters[code] = character
        
    def addDialog(self, code, input_text):
        text = ' - ' + input_text + ' - ' + self.dictionary.getRandomSayVerb() + ' ' + self.characters[code].getRandomName() + '.'
        self.writeParagraph(text)
