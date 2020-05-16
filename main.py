# bot.py
import wolframalpha
import wikipedia
# bot.py
import os
import random
import time

from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
API= os.getenv('WOLFRAM_ID')
bot = commands.Bot(command_prefix='!')

@bot.command(name='wolfy', help='Query the Wolfram|Alpha database')
async def wolfy(ctx, *args: str):
  final_arg = ""
  for arg in args:
    final_arg += arg + " "

  await ctx.send("Working on it..." + str(tries))
  WAclient = wolframalpha.Client(API)

  # Stores the response from
  # wolf ram alpha
  res = WAclient.query(final_arg)

  # Includes only text from the response
  try:
    answer = next(res.results).text
  except StopIteration:
    answer = "ERROR"

  await ctx.send("Here you go! ")
  await ctx.send(answer)


@bot.command(name="lookfor", help="Wikipedia")
async def wiki(ctx, *args: str):
  await ctx.send(random.choice(["Beaming it up", "Searching", "Scanning", "Looking on Ceti Alpha 5", "Searching Memory Alpha"])+'...')
  time.sleep(1.25)
  final_arg = ""
  for arg in args:
    final_arg += arg + " "
  await ctx.send(wikipedia.summary(final_arg))
  

keep_alive()
bot.run(TOKEN)
