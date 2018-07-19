# -*- coding: utf-8 -*-

import random

class Character:
    
    def __init__(self, code, names=[]):
        self.code = code
        self.names = names
        
    def getRandomName(self):
        return random.choice(self.names)
