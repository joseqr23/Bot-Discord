from django.shortcuts import render
import discord
import random

def index(request):

	# Config DiscordBot
	intents = discord.Intents.default()
	intents.message_content = True
	client = discord.Client(intents=intents)

	#Events
	@client.event
	async def on_ready():
		print(f'Bot {client.user} says hello world!')

	@client.event
	async def on_message(message):
		person = message.author # Persona que manda el mensaje
		
		if message.author == client.user:
			return

		# Function hola
		if message.content.startswith("!hola"):
			await message.channel.send(f"¡Mucho gusto, {person.mention}!")

		# Function joke	
		list_jokes = ['Se abre el ascensor y hay un programador dentro, le preguntan: - Sube o baja? A lo que el programador responde: - Si.','Que le dice un bit al otro? Nos vemos en el bus.', 'Atracador: El dinero o la vida! Programador: Lo siento, soy programador. Atracador: Y? Programador: No tengo dinero ni vida.','Que es un terapeuta? - 1024 Gigapeutas', 'Cuantos programadores hacen falta para cambiar una bombilla? - Ninguno, porque es un problema de hardware.','Se abre el telon, aparece un informatico y dice: que habeis tocado que no se cierra el telon!', '- ...fallece una persona mientras estudiaba en la biblioteca - Que estaba estudiando? - La API de Windows.','Que le dice un GIF a un JPG? -Animate hombre...', 'Que dice un informatico que se esta ahogando en la playa?: F1, F1!','Solo hay 10 tipos de personas en el mundo, las que entienden binario y las que no.','Solo hay 10 tipos de personas en el mundo: las que entienden trinario, las que no, y las que lo confunden con binario.','Una mujer dice a su marido informatico: - Ve al supermercado y trae una barra de pan, y si hay huevos, doce. Trajo doce barras de pan.','Quien demonios es el general Failure, y que hace intentando leer de mi disco duro?', 'En que se diferencian Windows y un virus? En que el virus funciona, y es gratis.', "Si debugear es eliminar errores del codigo, escribir es agregarlos.", "¿Qué es una mujer objeto? Una instancia de una mujer con clase.", "Se abre el telón, aparece un informático y dice: ¡qué habéis tocado que no se cierra el telón!.", "¿Pero qué haces tirando esos portátiles al río? - ¡Pero mira como beben los PC's en el rió!.", "Están 1023 gigabytes en una fiesta, llegan 1048576 más y dicen: ¿Nos hacemos un peta?.", "¿Cuál es la diferencia entre batman y Bill Gates? Que cuando batman luchó contra el pingüino ganó.", "La barriga de un programador es directamente proporcional a la cantidad de información que maneja.", "Dios es real, a no ser que lo declares como integer.", "Dos programadores dialogando sobre sus relaciones con su pareja: Yo tengo un vínculo muy fuerte con mi mujer. Entonces, tienes un hipervínculo?.", "-Prométeme que cuidarás a los niños y que les hablarás de mí.-¿Ya has vuelto a poner tus síntomas en Google? -Te quiero mucho...", "Esto es el cielo.Un ángel está hablando con Dios y le dice: - ¡Oh, Señor! en la Tierra descubrieron el código del Genoma Humano, - ¡Malditos Hackers!, responde Dios. Voy a tener que cambiar la contraseña.", "Vndo tclado casi nuvo a bun prcio solamnt falla una tcla."]
		random_jokes = random.choice(list_jokes)
		if message.content.startswith("!joke"):
			await message.channel.send(random_jokes)

		# Function tip
		tip_list = ["No te despedirán del trabajo, si nunca comentas tu código y además eres el único que sabe cómo funciona.","Aprende las bases de la programación antes de aprender un lenguaje específico.","Practica y experimenta con diferentes lenguajes y herramientas.", "Haz seguimiento de tus progresos y sigue aprendiendo constantemente.","Escribir código limpio y legible es esencial.", "Utiliza control de versiones para mantener un registro de los cambios en tu código.", "Aprende a depurar y resolver problemas.", "Trabaja en proyectos colaborativos y aprende a trabajar en equipo.","Utiliza la documentación y los recursos en línea para ayudarte en tus proyectos.","Aprende a comunicarte eficazmente tanto con tus compañeros de equipo como con tus clientes.","Mantén una actitud positiva y aprende a disfrutar el proceso de resolver problemas.","Aprende a pensar de manera algorítmica y lógica, esto te ayudará a resolver problemas de manera eficiente.","Aprende a optimizar tu código para mejorar el rendimiento y la escalabilidad.","Aprende a usar y entender las herramientas de depuración para detectar y solucionar errores.","Aprende a usar las herramientas de seguimiento de problemas para gestionar y solucionar los problemas en tus proyectos.","Aprende a trabajar con bases de datos y a comprender los principios de la programación orientada a objetos.","Aprende a usar una variedad de herramientas y librerías para extender tus habilidades de programación.","Aprende a trabajar en ambientes de desarrollo distribuidos y a entender los principios de la infraestructura de software.","Aprende a usar y entender las pruebas automatizadas para garantizar la calidad de tu código.","Aprende a usar herramientas de automatización para mejorar tu productividad y eficiencia.","Aprende a entender y mejorar la seguridad de tu código y sistemas."]
		random_tip = random.choice(tip_list)
		if message.content.startswith("!tip"):
			await message.channel.send(random_tip)

	return render(request, app = client.run("BOT_TOKEN")
)