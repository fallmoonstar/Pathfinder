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
        ame = discord.File(random_ame)
        await ctx.send(file= ame)

    @commands.command()
    async def 網圖(self, ctx):
        random_ame = random.choice(jdata["url_ame"])
        await ctx.send(random_ame)

def setup(bot):
    bot.add_cog(React(bot)) 