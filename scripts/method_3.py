import discord
from discord_easy_commands import EasyBot

intents = discord.Intents.default()
intents.message_content = True

bot = EasyBot(command_prefix='!', intents=intents)

# Events
@bot.event
async def on_ready():
    print(f'Bot {bot.user} says hello world!')

bot.setCommand("!hola", "Hola!")
bot.setCommand("!ping", "pong")

bot.run("BOT_TOKEN")