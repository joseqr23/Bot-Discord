import discord
from discord.ext import commands
from urllib import parse, request # Parse procesa una respuesta de una página, request permite enviar peticiones
import re # Expresiones regulares

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!",intents=intents)

# Events
@bot.event
async def on_ready():
    print(f'Bot {bot.user} says hello world!')

@bot.command()
async def ping(ctx):
	await ctx.send("pong")

@bot.command()
async def youtube(ctx, *, search):
	query = parse.urlencode({ 'search_query': search }) # Search es el texto que el usuario envía y parse se encarga de convertir el texto a una dirección de internet
	html_content = request.urlopen("http://www.youtube.com/results?"+query) # Obtener link de youtube
	
	# 1 - Buscará una frase o párrafo que empiece con href dentro del html_content
	# 2 - Con la expresión regular extraemos el id de los videos que obtenemos como resultados de nuestra búqueda
	search_results = re.findall(r'watch\?v=(.{11})', html_content.read().decode())
	print(search_results)
	if search_results:
		await ctx.send("https://www.youtube.com/watch?v="+search_results[0]+"\n"+"https://www.youtube.com/watch?v="+search_results[1])
	else:
		await ctx.send("No se han encontrado resultados.")

bot.run("BOT_TOKEN")
