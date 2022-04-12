from itertools import count
import discord
from discord.ext import commands
from core.classes import Cog_Extension
import re

class Vote(Cog_Extension):

    @commands.command()
    async def vote(self, ctx, *, cho):
        list = re.compile(r"\S+").findall(cho)
        emoji_num = [":one:",":two:",":three:",":four:",":five:",":six:",":seven:",":eight:",":nine:",":keycap_ten:"]

        if len(list) > 1:
            embed = discord.Embed(title = list[0],color=0x0011ff)
            list .pop(0)
            count = 0
            for ele in list:
                embed.add_field(name = f"{emoji_num[count]} {ele}", value = "\u200b", inline = False)
                count = count+1
            msg = await ctx.send(embed=embed)
            count = 0
            for ele in list:
                await msg.add_reaction(emoji_num[count])
                count = count+1
            
            else:
                embed = discord.Embed(title = "咖哩拌不拌?", color=0x0011ff)
                embed.add_field(name = list[0], value = "\u200b", inline = False)
                msg = await ctx.send(embed=embed)
                await msg.add_reaction(":ok:")
                await msg.add_reaction(":ng:")

            await ctx.message.delete()

def setup(bot):
    bot.add_cog(Vote(bot))
