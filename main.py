import discord
import os
from dotenv import load_dotenv
from discord.ext import commands
from utility import *

load_dotenv()

#Sets intents
intents = discord.Intents.default()
intents.message_content = True
intents.members = True

#Some basic setup. Help command is disabled to allow custom one to work properly
token = os.getenv('TOKEN')
bot = commands.Bot(command_prefix='./', description="KeaneBot", intents=intents, help_command=None)

#Login status message
@bot.event
async def on_ready():
    print("Bot started. Logged in as {0.user}".format(bot))

@bot.tree.command()
async def ping(interaction: discord.Interaction) -> None:
    """Ping the bot."""
    await interaction.response.send_message("Pong! :ping_pong:")

#Actually runs the thing
bot.run(token)
