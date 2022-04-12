import discord
from discord.ext import commands
from core.classes import Cog_Extension
import json
import random

with open("setting.json",mode="r",encoding="utf8") as jfile:
    jdata = json.load(jfile)


class Event(Cog_Extension):

    @commands.Cog.listener()
    async def on_member_join(self, member):
        channel = self.bot.get_channel(int(jdata["Welcome_Channel"]))
        await channel.send(f"@here {member} join!")
        print(f"{member} join!")

    @commands.Cog.listener()
    async def on_member_remove(self, member):
        channel = self.bot.get_channel(int(jdata["Leave_Channel"]))
        await channel.send(f"@here {member} leave!")
        print(f"{member} leave!")

    @commands.Cog.listener()
    async def on_message(self, msg):
        if msg.content.endswith('阿梅'):
            await msg.channel.send('我婆!!!!!')
        random_smile = random.choice(jdata["smile"])
        await msg.send(random_smile)
    

    

def setup(bot):
    bot.add_cog(Event(bot)) 