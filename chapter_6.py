# -*- coding: utf-8 -*-

from theater_writer import TheaterWriter
from novel_writer import NovelWriter

author = 'Gabo'
chapter_number = 6
chapter_title = 'Patrons'

writer = TheaterWriter(author, chapter_number, chapter_title)		

writer.addCharacter('andreu', ['Andreu Pasternak', 'el huérfano', 'el vengador', 'el niño bien', 'el heredero','Pasternak junior', 'Pasternak hijo', 'Andreu'])
writer.addCharacter('magrebi', ['el magrebí', 'el jefe', 'el traficante', 'el extranjero'])
writer.addCharacter('claudia', ['Clàudia', 'la policía', 'la chica hidrocarburo', 'la sotinspectora'])
writer.addCharacter('viladrau', ['Viladrau', 'el inspector', 'el inspector Viladrau'])
writer.addCharacter('freeman', ['Jordan Freeman', 'Jordan', 'Freeman', 'el ser artificial', 'el robot', 'el viejo'])
writer.addCharacter('musk', ['Nikola Musk', 'Nikola', 'el señor Musk', 'el inventor', 'el multimillonario', 'el CO de Hooper Tech'])
writer.addCharacter('cardenales', ['Carnedales', 'la inspectora Cardenales', 'la inspectora de la CNP', 'la tuerta'])
writer.addCharacter('abdal', ['Abdal', 'el enchufado', 'el magreví junior', 'el matón familiar'])

writer.narrate('Era un nuevo día en la bella Barceloneta, aunque el cielo seguía oscuro como en noche cerrada. Hacía mucho viento, y las señeras parecían a punto de reclamar su propia independencia respecto a los balcones que las sujetaban.')
writer.narrate('Poco sospechaba Úrsula que aquel seria el día de su propia muerte. Es decir, no es que fuera a morir ese día, simplemente que no pensaba en ello. Estaba tranquila, en contraste con la paranoia de los últimos días.')
writer.narrate('La asesina de Pasternak había dedicado la última noche a meditar en profundidad acerca de su actual situación. Matar al CEO de Iberdrola no iba a tener el efecto que ella deseaba, y seguir matando a otros empresarios, aunque esta vez fueran catalanes... no parecía lo más sensato como siguiente paso. La policía es lenta, pero no tonta: acabarían notando sus patrones, y la acabarían deteniendo. Demasiados cabos sueltos... cabos que había que quemar, antes de proseguir con sus planes.')

writer.addIntermission('a bastantes metros bajo tierra')

writer.addDialog('andreu', '¡¿Qué es esta puta mierda?!')
writer.narrate('Pasternak hijo lanzó el librito sobre la mesa, sin obtener reacción alguna de su interlocutor más allá de la sorna y la despreocupación.')
writer.narrate('Se encontraba en una improvisada sala de los subterráneos de Barcelona, la cual había sido creada a partir de uno de los largos túneles, básicamente cubriendo los dos extremos con muros de ladrillo y colocando una puerta en cada uno. Ante él, un hombre magrebí armado descansaba sobre un taburete, con matones iguamente armados cubriéndole derecha e izquierda.')
writer.addDialog('magrebi', 'Papel. Uno no puede andar registrando ventas de codificadores de ADN en la nube: los bots de google te encontrarían en medio segundo')
writer.narrate('Andreu golpeó la mesa con ambos brazos, ante lo cual los dos guardias hicieron ademán de empuñar sus pistolas. El magrebí les detuvo con un gesto.')
writer.addDialog('andreu', '¿Me estás diciendo que el codificador que se utilizó en el... asesinato de mi padre... fue comprado por él mismo?')
writer.addDialog('magrebi', 'O por alguien que usaba su nombre. Ya sabes, no solemos pedir documento de identidad por aquí... en fin, ¿Hay algo más que podamos hacer por usted, señor heredero?')
writer.narrate('El traficante hizo ademán de agarrar de la mesa las dos tarjetas de crédito que le había entregado el huérfano momentos antes, pero justo en ese momento alguien abrió la puerta a espaldas de Pasternak.')
writer.narrate('Entró en la sala la mujer tuerta que daba la bienvenida a los clientes de aquel dudoso negocio, seguida por un afroamericano de unos sesenta años. Se parecía muchísimo a ese actor fallecido del siglo pasado, aunque algo más calvo y gordo.')
writer.addDialog('magrebi', 'Vaya... parece que ha llegado el siguiente cliente: tendrá que pedir hora para otro día')
writer.narrate('Pasternak entrecerró los ojos: no pensaba dejarle a ese capullo todo su dinero a cambio de nada de información, pero escapar de allí solo parecía posible a través de la puerta situada tras el capo... y sus dos guardias. No tenía tiempo de sentarse a observar sus patrones de comportamiento y encontrar la manera de burlarlos: debía actuar.')

writer.addIntermission('en la base central dels mossos')

writer.addDialog('viladrau', 'Has enviat a la caríssima IA d\'en Nikola Musk a què s\'infiltri a una guarida de traficants de codificadors?!')
writer.narrate('Él y su sotinspectora, Clàudia, se encontraban en una sala llena de agentes moviéndose de arriba a abajo. Varios de ellos se pararon a mirar a la pareja, pero Clàudia les indicó con la mirada que no era buena idea meterse en sus asuntos.')
writer.addDialog('claudia', 'Freeman es va oferir, inspector. I tenint en compte la perillositat de la missió, i que en Pasternak a mi ja em coneix, pareixia l\'opció més lògica')
writer.narrate('El inspector se disponía a continuar riñéndola, con la vena del cuello cada vez más hinchada, cuando su móvil, que reposaba sobre el escritorio de Clàudia, comenzó a sonar. En la pantalla táctil podía verse el nombre "Nikola Musk".')
writer.narrate('Vilarnau tragó saliva y cogió su dispositivo. Dibujó el patrón en la pantalla, aunque no era necesario, y los nervios le dificultaron acertar con el botón de contestar.')

writer.addIntermission('a muchos metros bajo tierra')

writer.addDialog('freeman', 'Buenas tardes, me han comentado que aquí puedo encontrar codificadores de... un momento, ¿Qué es ese ruido?')
writer.addDialog('magrebi', '¿Cómo? Yo no oigo nada...')
writer.addDialog('freeman', '¡Shhh...! Creo que viene de esa pared de la derecha...')
writer.addDialog('magrebi', '... Jim, haz el favor de ir a ver si hay alguna rata correteando por ahí...')
writer.addDialog('freeman', 'Ehm... no, no, esa pared no. Me refería a la pared de mi derecha, no la vuestra... perdón')
writer.narrate('El traficante le miró irritado, pero entonces posó sus ojos sobre algo llamativo de dicha pared. Había una luz roja parpadeante. Y... ahora que todo el mundo había callado al fin... sí que se oía algo... algo así como un pitido intermitente...')
writer.narrate('El instinto le gritó a Pasternak hijo que corriera, y eso hizo, tras agarrar a la carrera sus dos tarjetas de crédito y el libro de cuentas. Se encontraba cerca de la puerta trasera, rezando porque no estuviera cerrada... cuando un fogonazo de luz y un terrible estruendo cubrieron toda la sala.')

writer.addIntermission('de nuevo bajo el bello cielo despejado de Barcelona')

writer.narrate('Úrsula sonrió para sí. Sostenía aún el dispositivo de control remoto con el que acababa de detonar las bombas que había colocado aquella misma mañana en el túnel. Seguramente ni ése magrebí conocía su verdadera identidad, pero no podía correr riesgos. Además, a veces hay que enterrar el pasado para seguir avanzando. Era un patrón que se repetía en su vida, y siempre le conducía a una situación mejor.')

writer.addIntermission('en algún lugar del cielo barcelonés')

writer.narrate('Nikola Musk miró el móvil que sostenía en su mano derecha con indiferencia. En los altavoces del aparato sonaba el buzón de voz. Parecía que el inspector andaba muy ocupado.')
writer.narrate('El magnate suspiró y dio un sorbo a su mojito. Desde la ventanilla del avión podía ver la sagrada familia: la primera vez que la veía terminada. Una maravilla, sin duda... aunque no parecía merecer tanta espera. Sacudió la cabeza: no lograba quitarse de encima esa preocupación por el bienestar de Jordan Freeman. Había perdido la señal del localizador, lo cual podía deberse a un fallo o... que se encontrara en algún lugar incomunicado.')
writer.addDialog('musk', 'Es como dar diamantes a los cerdos... no saben aprovechar el potencial de mis productos... siempre se repite el mismo patrón con los humanos')

writer.addIntermission('en los túneles')

writer.narrate('Freeman nunca perdía la conciencia, por lo que presenció todo lo que acababa de ocurrir en la medida en que su vista y oído de calidad humana le permitieron. Se habían producido dos explosiones: una en la misma sala en la que se encontraban y la otra, al parecer al otro lado de la puerta que se encontraba tras el magrebí.')
writer.narrate('Parte del túnel se había derrumbado con un estruendo, y la instalación eléctrica había fallado; por lo que se encontraban a oscuras. Él no podía desplazarse con normalidad, pues parte del muro había caído sobre su cuerpo, aprisionándole ambas piernas. No podía hacer más que apoyarse con los codos sobre el suelo cual adolescente en una fiesta de pijamas y llamar a los humanos supervivientes. No sentía dolor, pero la situación le resultaba harto frustrante.')
writer.narrate('Jordan escuchó un gemido unos metros más allá. Parecía una voz femenina, por lo que debía tratarse de la tuerta.')
writer.addDialog('freeman', '¡Inspectora Cardenales! ¿Se encuentra bien?')

writer.addDialog('cardenales', '... joder... ¡Calla puto robot! No te cargues mi tapadera... aquí soy una matona más del magrebí...')
writer.addDialog('freeman', '... ¿Cree que siguen vivos?')
writer.addDialog('cardenales', 'No sé... a ver, espera creo que estoy tocando un cuerpo... joder que oscuro está todo... ahh, mi cabeza... ¡Ah! Estoy tocando una cara... creo que es la del chaval del magrebí, su sobrino-nieto o algo así... Abdal')

writer.addDialog('abdal', 'Ah... ¡Quita, zorra! No me toques... eh, ¿Dónde estoy? No veo una mierda')
writer.addDialog('freeman', 'Al parecer algún tipo de explosión detonó en la sala y se derrumbó parte del muro...')
writer.addDialog('abdal', '¡No jodas! ¿Y mi tío-abuelo? Joder, a ver... ¿Habéis encontrado alguno el escritorio? En uno de los cajones tendría que haber linternas... el jefe siempre tenía alguna por si acaso')
writer.addDialog('freeman', 'Yo tengo las piernas atrapadas... no me puedo mover')
writer.addDialog('abdal', '... bah, ya lo he encontrado... a ver...')
writer.narrate('Un haz de luz se originó de repente y le dio a Freeman de lleno en la cara. Cuando se apartó, pudo ver a un joven magrebí, uno de los guardias que había visto al lado del capo, sosteniéndola.')
writer.addDialog('abdal', '¡Tío! ¡Tío, ¿Dónde estás?! Joder...')
writer.addDialog('cardenales', 'Eh... ¿Has encontrado la linterna al final o qué?')
writer.addDialog('abdal', '¿Qué dices estúpida? Si la tengo aquí, y te estoy apuntando con... ostia puta, te sangra la frente a saco...')
writer.narrate('Al parecer, Cardenales había recibido el impacto de algún escombro sobre el ojo sano, que le sangraba profusamente. La mujer se tocó la cara, y tras un tenso minuto de asimilación, gritó y lloró.')
writer.addDialog('cardenales', '¡Estoy ciega! Joder, no puede ser... no veo nada... no me lo creo. ¡Hijos de puta! No me vaciléis, no hay luz ni ostias... es mentira...')
writer.addDialog('freeman', 'Tranquilícese, señorita. La llevaremos al hospital en cuanto salgamos de aquí...')
writer.addDialog('abdal', 'Eso será si salimos...')
writer.narrate('Abdal recorrió toda la pequeña estancia con la linterna. La parte trasera de la estancia se había derrumbado parcialmente, taponando la puerta trasera. La puerta principal aún era accesible, aunque al parecer el derrumbamiento había ejercido mucha presión sobre ella y era imposible abrirla. Tampoco disponían de un soplete o de una palanca para intentar forzarla. En definitiva: estaban atrapados allí.')
writer.addDialog('abdal', 'Puta vida...')
writer.addDialog('magrebi', 'Ab...dal...')
writer.narrate('El joven corrió hacia la voz de su tío-abuelo, que surgía de debajo de unos escombros cercanos al escritorio. Tras apartarlos, Abdal comprobó con horror que su jefe y familiar había recibido un buen golpe en la cabeza, y se encontraba entre la vigilia y la inconsciencia.')
writer.addDialog('abdal', 'Tío... no te preocupes, te sacaré de aquí...')
writer.addDialog('andreu', '... ¡Eh...! ¿Me oís?')
writer.narrate('Todos se sobresaltaron al escuchar de voz del heredero Pasternak proviniendo de la pared derrumbada. Se miraron con caras de sorpresa y esperanzas renovadas, menos la ciega, claro está.')
writer.addDialog('abdal', '¡Eh! ¡Sí, Pasternak, estamos aquí! ¡Ja, ja, ja, que suerte! Escucha, avanza por el túnel y llegarás a otra sala donde descansan los hombres de mi tío... diles lo que ha ocurrido...')
writer.addDialog('andreu', 'Ya me gustaría... pero estoy atrapado, se ha derrumbado una parte del muro y la puerta parece haberse atrancado... está como doblada por la presión... no, espera... no me digas que tú también...')
writer.addDialog('abdal', '¡Joder! ¡JODER! Vaya puta mierda, también está atrapado... ¡Eh! ¿Está Micky contigo?')
writer.addDialog('andreu', '¿El grandullón que estaba con vosotros? No está aquí... lo mismo él consiguió escapar...')
writer.addDialog('abdal', 'No lo creo. Tú eres el primero que echó a correr... ¿Has sido tú, hijo de puta? Querías jodernos y te has jodido a ti también?')
writer.addDialog('andreu', '¿Estás de coña? Sé tanto del tema como tú. Tan solo tuve un mal presentimiento con el tema del pitido y tal')
writer.addDialog('abdal', 'Ya veo... entonces fuiste tú, negro')
writer.narrate('Con un rápido movimiento, el joven magrebí desenfundó su arma y apuntó a Jordan a la cabeza. Freeman levantó los brazos en señal de rendición, pero su torso continuó erguido sobre su ombligo, como si sus abdominales fueran de puro hierro.')
writer.addDialog('abdal', 'Eso que te sale de debajo de las piernas... parece sangre, pero es muy negra... tú... tú no eres humano, tío, ¿Verdad?')
writer.addDialog('freeman', 'Soy una IA, pero no soy quién ha ocasionado esto. Como ves, estoy en peor condición que tú incluso')
writer.addDialog('andreu', 'Chicos... ¡Chicos! ¿No oléis como a gas?')
writer.narrate('Se produjo un tenso silencio mientras el criminal y el ser artificial que ahora ejercía de policia se miraban a los ojos.')
writer.addDialog('abdal', '¿Qué? No...')
writer.addDialog('cardenales', 'Yo no huelo nada raro... y tengo buen olfato para estas cosas')
writer.addDialog('andreu', 'Vale, pues... por favor, no provoquéis ninguna chispa... creo que se ha roto una tubería y mi sala se está llenando de gas...')
writer.addDialog('abdal', 'De puta madre...')
writer.narrate('Andreu no había tenido una vida fácil, a pesar de ser rico y esas cosas. Es más, había comprobado más de una vez aquello de que las cosas siempre pueden empeorar. Era el único patrón de su vida que sabía que nunca dejaría de repetirse. Aunque aquella vez la cosa había llegado a otro nivel.')

writer.finish()
