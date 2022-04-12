import discord
from discord.ext import commands
from core.classes import Cog_Extension
import json
import random

with open("setting.json",mode="r",encoding="utf8") as jfile:
    jdata = json.load(jfile)

class React(Cog_Extension):

    @commands.command()
    async def 阿梅(self, ctx):
        random_ame = random.choice(jdata["ame"])
        await ctx.send(random_ame)

    @commands.command()
    async def 願望(self, ctx):
        random_hope = random.choice(jdata["hope"])
        await ctx.send(random_hope)

    @commands.command()
    async def 頭貼(self, ctx):
        random_icon = random.choice(jdata["icon"])
        await ctx.send(random_icon)

    @commands.command()
    async def 想瑟瑟(self, ctx):
        random_18 = random.choice(jdata["18"])
        await ctx.send(random_18)
        await ctx.send(f"不可以色色ˋAˊ")

def setup(bot):
    bot.add_cog(React(bot)) 