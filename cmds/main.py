import discord
from discord.ext import commands
from core.classes import Cog_Extension
import json
import datetime


class Main(Cog_Extension):

    @commands.command()
    async def ping(self, ctx):
        await ctx.send(f"{round(self.bot.latency*1000)} (ms)")

    @commands.command()
    async def hi(self, ctx):
        await ctx.send("Hi Friend")

    @commands.command()
    async def 說(self, ctx, *, msg):
        await ctx.message.delete()
        await ctx.send(msg)

    @commands.command()
    async def clean(self, ctx, num: int):
      await ctx.channel.purge(limit=num+1)

    @commands.command()
    async def 發財(self, ctx):
        await ctx.send(f"拉進來 打出去 馬文發大財")

    @commands.command()
    async def about(self, ctx):
        embed=discord.Embed(title="關於探路者", url="https://github.com/fallmoonstar/Pathfinder", description="Pathfinder", color=0x1feae7, 
        timestamp= datetime.datetime.now())
        embed.set_image(url="https://images6.alphacoders.com/112/1123225.jpg")
        embed.set_author(name="落月", url="https://github.com/fallmoonstar", icon_url="https://picrew.me/shareImg/org/202204/516657_x6yBdHqG.png")
        embed.set_thumbnail(url="https://s1.zerochan.net/Watson.Amelia.600.3549767.jpg")
        embed.add_field(name="作者discord", value="闇·維爾特·落月星輝#3277", inline=False)
        embed.add_field(name="圖奇", value="https://www.twitch.tv/fm_ash_", inline=True)
        embed.add_field(name="YT", value="https://www.youtube.com/channel/UCyZ2oYL24iL2Jmn4LkcOHYA", inline=True)
        embed.add_field(name="伺服器", value="https://discord.gg/HkGq4tMxXR", inline=False)
        embed.set_footer(text="自主學習專用")
        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(Main(bot)) 