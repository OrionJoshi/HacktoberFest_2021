# Discord Bot

import discord
from discord.ext import commands

bot = commands.Bot(command_prefix="!")

@bot.event
async def on_connect():
  print ("Hi! I am here")

@bot.command()
async def test(ctx):
  await ctx.send ("Hello")

# Do not share token with anyone - ultimate key tot he discord account
# Steps to retrieve token available on the internet
token = (" xyz ")
bot.run(token)


