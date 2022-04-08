from email.contentmanager import raw_data_manager
from http.client import ImproperConnectionState
import discord
from discord.ext import commands
import json
import random
import os

with open("setting.json",mode="r",encoding="utf8") as jfile:
    jdata = json.load(jfile)

#intens為特殊權限管理 member要額外開
intents = discord.Intents.default()
intents.members = True

print("Hello world")
#BOT指令為^
bot = commands.Bot(command_prefix='^',intents = intents)
#上線後回傳到黑窗
@bot.event
async def on_ready():
    print(">> BOT is online <<")
#BOT事件 加入與離開   
@bot.event
async def on_member_join(member):
    channel = bot.get_channel(int(jdata["Welcome_Channel"]))
    await channel.send(f"@here {member} join!")
    print(f"{member} join!")

@bot.event
async def on_member_remove(member):
    channel = bot.get_channel(int(jdata["Leave_Channel"]))
    await channel.send(f"@here {member} leave!")
    print(f"{member} leave!")

@bot.command()
async def load(ctx, extension):
    bot.load_extension(f'cmds.{extension}')
    await ctx.send(f'Loaded {extension} done.')

@bot.command()
async def unload(ctx, extension):
    bot.unload_extension(f'cmds.{extension}')
    await ctx.send(f'Un - Loaded {extension} done.')

@bot.command()
async def reload(ctx, extension):
    bot.reload_extension(f'cmds.{extension}')
    await ctx.send(f'Re - Loaded {extension} done.')

for filename in os.listdir('./cmds'):
    if filename.endswith('.py'):
        bot.load_extension(f'cmds.{filename[:-3]}')

@bot.command()
async def 探路者(ctx):
    random_N3 = random.choice(jdata["N3"])
    N3 = str(random_N3)
    await ctx.send(N3)

#RUNbot
if __name__ == "__main__":

    bot.run(jdata["TOKEN"])