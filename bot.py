from email.contentmanager import raw_data_manager
from http.client import ImproperConnectionState
import discord
from discord.ext import commands
import json
import random

with open("setting.json",mode="r",encoding="utf8") as jfile:
    jdata = json.load(jfile)

#intens為特殊權限管理 member要額外開
intents = discord.Intents.default()
intents.members = True


#BOT指令為$
bot = commands.Bot(command_prefix='$',intents = intents)
#上線後回傳到黑窗
@bot.event
async def on_ready():
    print(">> BOT is online <<")
#BOT事件 加入與離開   
@bot.event
async def on_member_join(member):
    channel = bot.get_channel(int(jdata["Welcome_Channel"]))
    await channel.send(f"@everyone {member} join!")
    print(f"{member} join!")

@bot.event
async def on_member_remove(member):
    channel = bot.get_channel(int(jdata["Leave_Channel"]))
    await channel.send(f"@everyone {member} leave!")
    print(f"{member} leave!")
#  BOT$指令
@bot.command()
async def ping(ctx):
    await ctx.send(f"{round(bot.latency*1000)} (ms)")

@bot.command()
async def number5(ctx):
    random_N5 = random.choice(jdata["N5"])
    N5 = str(random_N5)
    await ctx.send(N5)

@bot.command()
async def 早安(ctx):
    await ctx.send(f"早安")

@bot.command()
async def 圖片(ctx):
    random_pic = random.choice(jdata["pic"])
    pic = discord.File(random_pic)
    await ctx.send(file= pic)

#RUNbot
bot.run(jdata["TOKEN"])