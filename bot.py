import logging
import random
import discord
import os
import math
from test import *
from discord.ext import commands

logging.basicConfig(level=logging.INFO)
images = os.listdir("./food")



description = '''the best discord bot ever created'''
bot = commands.Bot(command_prefix='!', description=description)

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

@bot.command()
async def yoyoyo(ctx):
    """Says something"""
    await ctx.send("harry is a shamless tinker picker")

@bot.command()
async def yoyo(ctx):
    """does something"""
    for x in range (1,10):
        await ctx.send("harry is a shamless tinker picker")
    await ctx.send("hes also only 2k")

@bot.command()
async def hero(ctx):
    """does pick a random hero"""
    file = open('heroes.txt', 'r')
    list1 = list(file.readlines())
    file.close()
    H = random.choice(list1)
    await ctx.send(H)

@bot.command(pass_context = True)
async def yo(ctx):
    """does antoher thing"""
    await ctx.send(file=discord.File('image.png'))

@bot.command(pass_context = True)
async def asdf(ctx):
    """use on weirdos"""
    await ctx.send('what is wrong with you', file=discord.File('weird2.jpeg'))

@bot.command(pass_context = True)
async def food(ctx):
    """use when hungry"""
    imgStr = random.choice(images)
    path = "./food/" + imgStr
    await ctx.send(file=discord.File(path))

@bot.command()
async def add(ctx, *args):
    """Adds numbers together."""
    if len(args) == 0:
        await ctx.send("you're stupid lol")
        return
    
    result = 0
    list = []
    
    try:
        for x in range (len(args)):
            list.append(float(args[x]))
            result = result + list[x]
        if math.isinf(result) or math.isnan(result):
            await ctx.send("value(s) too extreme wtf are you doing")
        elif result.is_integer():
            await ctx.send(math.floor(result))
        else:
            await ctx.send(result)
    except:
        await ctx.send('are you stupid')
        
bot.run(TOKEN)