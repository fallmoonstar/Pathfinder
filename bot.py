import discord
from discord.ext import commands
import json
import random
import os
import keep_alive

with open("./setting.json",mode="r",encoding="utf8") as jfile:
    jdata = json.load(jfile)

#intens為特殊權限管理 member要額外開
intents = discord.Intents.default()
intents.members = True

#print("Hello world")
#BOT指令為^
bot = commands.Bot(command_prefix='^',intents = intents)
#上線後回傳到黑窗
@bot.event
async def on_ready():
    print(">> BOT is online <<")

@bot.command()
async def load(ctx, extension):
    bot.load_extension(f'cmds.{extension}')
    await ctx.send(f'載入 {extension} 完成.')

@bot.command()
async def unload(ctx, extension):
    bot.unload_extension(f'cmds.{extension}')
    await ctx.send(f'關閉 {extension} 完成.')

@bot.command()
async def reload(ctx, extension):
    bot.reload_extension(f'cmds.{extension}')
    await ctx.send(f'重置 {extension} 完成.')

for filename in os.listdir('./cmds'):
    if filename.endswith('.py'):
        bot.load_extension(f'cmds.{filename[:-3]}')

bot.remove_command("help")

@bot.command(name = 'help')
async def help(ctx):
    embed=discord.Embed(title="help", description="指令表", color=0x007bff)
    embed.add_field(name="回覆", value="^about,^hi,^ping,^發財,^探路者,^最近在聽的歌", inline=False)
    embed.add_field(name="圖片", value="^阿梅,^頭貼,^願望,^想瑟瑟", inline=True)
    await ctx.send(embed=embed)

@bot.command()
async def 探路者(ctx):
    random_N3 = random.choice(jdata["N3"])
    N3 = str(random_N3)
    await ctx.send(N3)

#RUNbot
if __name__ == "__main__":
    keep_alive.keep_alive()
    bot.run(jdata["TOKEN"])