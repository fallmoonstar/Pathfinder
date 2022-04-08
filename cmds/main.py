import discord
from discord.ext import commands
from core.classes import Cog_Extension

class Main(Cog_Extension):

    @commands.command()
    async def ping(self, ctx):
        await ctx.send(f"{round(self.bot.latency*1000)} (ms)")

    @commands.command()
    async def hi(self, ctx):
        await ctx.send("Hi Friend")

    @commands.command()
    async def 早安(self, ctx):
        await ctx.send(f"早安吶早安吶")

    @commands.command()
    async def 晚安(self, ctx):
        await ctx.send(f"祝各位有個好夢")

    @commands.command()
    async def 發財(self, ctx):
        await ctx.send(f"拉進來 打出去 馬文發大財")

def setup(bot):
    bot.add_cog(Main(bot)) 