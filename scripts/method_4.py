import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

# Events
@bot.event
async def on_ready():
    print(f'Bot {bot.user} says hello world!')

@bot.command()
async def saludo(ctx): # Cada función es un comando en discord !saludo
  author = ctx.message.author
  await ctx.send(f"¡Hola {author.mention}!")

bot.run("BOT_TOKEN")
