# -*- coding: utf-8 -*-

from writer import Writer

writer_name = 'Gabo'
chapter_number = 6
chapter_title = 'Patrones'

write = Writer(writer_name, chapter_number, chapter_title)		

write.narrate('Era un nuevo día en la bella Barceloneta. Hacia mucho viento, y las banderas independendistas parecían a punto de reclamar su propia independencia respecto a los balcones que las sujetaban')
write.narrate('Poco sospechaba Úrsula que aquel seria el día de su propia muerte')

write.end()
