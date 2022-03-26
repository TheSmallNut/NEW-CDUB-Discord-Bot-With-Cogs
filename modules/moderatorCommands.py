from discord.ext import commands
import discord
import os


class moderatorCommands(commands.Cog, name="Moderator"):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="getMembers", aliases=[])
    @commands.has_permissions(administrator=True)
    async def _getMembers(self, ctx: commands.Context):
        for member in ctx.guild.members:
            print(member)


def setup(bot):
    print("Moderator Cog Loaded")
    bot.add_cog(moderatorCommands(bot))


def teardown(bot):
    print("Moderator Cog Unloaded")
