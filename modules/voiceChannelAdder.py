from discord.ext import commands
import discord
import os


class voiceChannelAdder(commands.Cog, name="Voice_Channel"):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="cloneVoiceChannel", aliases=["cvc"])
    @commands.has_permissions(administrator=True)
    async def _cloneVoiceChannel(self, ctx: commands.Context, channelID):
        channel = self.bot.get_channel(int(channelID))
        newChannel = await channel.clone(name="TESTING", reason="This has been automatically done by CDUB Bot")
        await newChannel.move(after=channel)

    @commands.Cog.listener()
    async def on_voice_state_update(self, member, before, after):
        if after.channel is not None:
            print(f"{member.name} joined a vc")


def setup(bot):
    print("Voice_Channel Cog Loaded")
    bot.add_cog(voiceChannelAdder(bot))


def teardown(bot):
    print("Voice_Channel Cog Unloaded")
