import os
import disnake
import wl_magixx

from disnake.ext import commands, tasks
from pathlib import Path

path = Path(wl_magixx.__file__)

bot = commands.Bot(command_prefix = ".", help_command=None, intents = disnake.Intents.all())


@bot.event
async def on_ready():
    for filename in os.listdir(f"{str(path.parent)}/discordbot/cogs"):
        if filename.endswith(".py"):
            bot.load_extension(f"wl_magixx.discordbot.cogs.{filename[:-3]}")

def run(TOKEN_BOT: str):
    bot.run(TOKEN_BOT)