import discord as Ballspy
from Ballspy.ext import commands as BallsCommands

Balls = BallsCommands.bot(command_prefix="sex")

@Balls.event
async def on_ready():
  print("balls")
  
@Balls.command()
async def balls(ctx):
  await ctx.send("balls")
Balls.run("balls")
