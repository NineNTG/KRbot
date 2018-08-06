import discord
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio

bot = commands.Bot(command_prefix="!")

@bot.event
async def on_ready():
    print ("Online.")

@bot.command(pass_context=True)
async def r1h(ctx, user: discord.Member):
    await bot.say("**FIRST CLEAR:** {} \n - GR Hard Boss: ***XAKIOS**.".format(user.name))
    await bot.delete_message(ctx.message)

@bot.command(pass_context=True)
async def r2h(ctx, user: discord.Member):
    await bot.say("**FIRST CLEAR:** {} \n - GR Hard Boss: **NUBIS**.".format(user.name))
    await bot.delete_message(ctx.message)

@bot.command(pass_context=True)
async def r3h(ctx, user: discord.Member):
    await bot.say("**FIRST CLEAR:** {} \n - GR Hard Boss: **GUSHAK**.".format(user.name))
    await bot.delete_message(ctx.message)

@bot.command(pass_context=True)
async def r4h(ctx, user: discord.Member):
    await bot.say("**FIRST CLEAR:** {} \n - GR Hard Boss: **NORDIK**.".format(user.name))
    await bot.delete_message(ctx.message)

@bot.command(pass_context=True)
async def r5h(ctx, user: discord.Member):
    await bot.say("**FIRST CLEAR:** {} \n - GR Hard Boss: **MAVIEL**.".format(user.name))
    await bot.delete_message(ctx.message)

@bot.command(pass_context=True)
async def r6h(ctx, user: discord.Member):
    await bot.say("**FIRST CLEAR:** {} \n - GR Hard Boss: **MANTICORE**.".format(user.name))
    await bot.delete_message(ctx.message)

@bot.command(pass_context=True)
async def atk(ctx,n: int,x:int):
    await bot.say("Guild buff **ATK** raised: {}% -> {}%.".format(n,x)) 
    await bot.delete_message(ctx.message)

@bot.command(pass_context=True)
async def conquest(ctx, n: int):
    if (n>1): await bot.say("Requested to participate in new upcoming Saturday Guild Conquest.")
    else: await bot.say("Requested to participate in new upcoming Tuesday Guild Conquest.")
    await bot.delete_message(ctx.message)

@bot.command(pass_context=True)
async def rank(ctx,n: int,m: int,e: int):
    if ((e-m)>0): await bot.say("Placed {} in the Guild Conquest while our global rank is now #{} (+{}).".format(n,m,e-m))
    else: await bot.say("Placed {} in the Guild Conquest while our global rank is now #{} ({}).".format(n,m,e-m))
    await bot.delete_message(ctx.message)   

    

bot.run("process.env.BOT_TOKEN")
