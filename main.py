from discord.ext import commands
import API.secret as secret
import os
from discord import Intents

intents = Intents.default()
intents.members = True
bot = commands.Bot(command_prefix='!', intents=intents)


def loadModules():
    # Change "cogs" to your folder name
    for filename in os.listdir("./modules"):
        if filename.endswith(".py"):
            bot.load_extension(f"modules.{filename[:-3]}")


loadModules()


bot.run(secret.TEST_BOT)
