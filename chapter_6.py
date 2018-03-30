# -*- coding: utf-8 -*-

from writer import Writer

author = 'Gabo'
chapter_number = 6
chapter_title = 'Patrons'

writer = Writer(author, chapter_number, chapter_title)		

writer.addCharacter('ursula', ['Úrsula', 'la asesina', 'la periodista', 'la criminal'])
writer.addCharacter('freeman', ['Jordan Freeman', 'Jordan', 'Freeman', 'el ser artificial', 'el robot'])
writer.addCharacter('cardenales', ['Carnedales', 'la inspectora Cardenales', 'la inspectora', 'la tuerta', 'la inspectora'])

writer.narrate('Era un nuevo día en la bella Barceloneta. Hacia mucho viento, y las señeras parecían a punto de reclamar su propia independencia respecto a los balcones que las sujetaban.')
writer.narrate('Poco sospechaba Úrsula que aquel seria el día de su propia muerte. Osea, no es que vaya a morir hoy, simplemente que no pensaba en ello. Estaba tranquila, en contraste con la paranoia de los últimos días.')
writer.addIntermission('a unos 200 metros bajo tierra')

writer.addDialog('freeman', 'Usted... usted es la inspectora Cardenales')
writer.addDialog('cardenales', '... creo que me confundes con otra persona. Mi trabajo se aleja bastante del mundo... legal')

writer.finish()
