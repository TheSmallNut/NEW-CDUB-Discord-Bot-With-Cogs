from discord.ext import commands
import discord
import os


class cog1(commands.Cog, name="cog1"):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="ping", aliases=[])
    @commands.has_permissions(administrator=True)
    async def _ping(self, ctx: commands.Context):
        ctx.send(f"Pong {round(self.bot.latency * 1000)}ms")


def setup(bot):
    print("cog1 Cog Loaded")
    bot.add_cog(cog1(bot))


def teardown(bot):
    print("cog1 Cog Unloaded")
