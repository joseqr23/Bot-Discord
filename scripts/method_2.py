import discord

# Config DiscordBot
intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

# Events
@client.event
async def on_ready():
    print(f'Bot {client.user} says hello world!')

@client.event
async def on_message(message):
	person = message.author # Persona que manda el mensaje
	
	if message.author == client.user:
		return
	
	if message.content.startswith("!hola"):
		await message.channel.send(f"¡Mucho gusto, {person.mention}!")
	

client.run('BOT_TOKEN')