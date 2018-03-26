# -*- coding: utf-8 -*-

from writer import Writer

author = 'Gabo'
chapter_number = 6
chapter_title = 'Patrons'

write = Writer(author, chapter_number, chapter_title)		

write.narrate('Era un nuevo día en la bella Barceloneta. Hacia mucho viento, y las banderas independendistas parecían a punto de reclamar su propia independencia respecto a los balcones que las sujetaban.')
write.narrate('Poco sospechaba Úrsula que aquel seria el día de su propia muerte. Osea, no es que vaya a morir hoy, simplemente que no pensaba en ello. Estaba tranquila, en contraste con la paranoia de los últimos días.')
write.changeContext('Mientras tanto, a unos 200 metros bajo tierra')

write.end()
