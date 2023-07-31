import discord
import os
from dotenv import load_dotenv
from discord.ext import commands
from discord import app_commands
from utility import *

import logging
from loguru import logger
import sys

intents = discord.Intents.default()
intents.message_content = True
intents.members = True
client = discord.Client(intents=intents)
tree = app_commands.CommandTree(client)

token = os.environ.get('TOKEN')
MY_GUILD = discord.Object(id=os.environ.get('MY_GUILD'))
bot = commands.Bot(command_prefix='./', description="KeaneBot", intents=intents, help_command=None)


class InterceptHandler(logging.Handler):
    """Intercept existing logging handlers with Loguru."""

    def emit(self, record: logging.LogRecord) -> None:
        """Emit a log to loguru."""
        try:
            level = logger.level(record.levelname).name
        except ValueError:
            level = record.levelno

        frame, depth = sys._getframe(6), 6
        while frame and frame.f_code.co_filename == logging.__file__:
            frame = frame.f_back
            depth += 1

        logger.opt(depth=depth, exception=record.exc_info).log(level, record.getMessage())

logging.basicConfig(handlers=[InterceptHandler()], level=logging.INFO, force=True)

@bot.event
async def on_ready():
    """Start the bot."""
    bot.tree.copy_global_to(guild=MY_GUILD)
    await bot.tree.sync(guild=MY_GUILD)
    logger.info(f"Bot started. Logged in as {bot.user}")

@bot.tree.command()
async def ping(interaction: discord.Interaction) -> None:
    """Ping the bot."""
    await interaction.response.send_message("Pong! :ping_pong:")

bot.run(token, log_handler=None)
