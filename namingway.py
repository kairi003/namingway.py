#!/usr/bin/env python3

import sys
import discord
from discord.ext import commands
import random
from typing import Optional

TOKEN = sys.argv[1]

intents = discord.Intents.all()
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.command()
@commands.guild_only()
@commands.has_role('Cecil')
async def nick(ctx: commands.Context, target:discord.Member, new_name: str):
    print(ctx.author, target, new_name)
    old_name = target.display_name
    await target.edit(nick=new_name)
    await ctx.send(f"<@{target.id}> renamed by <@{ctx.author.id}> ({old_name} -> {new_name})")

@bot.command()
@commands.guild_only()
@commands.has_role('Cecil')
async def ybb(ctx: commands.Context, _target: Optional[discord.Member], _new_name: Optional[str]):
    target = _target if _target else ctx.author
    yubaba = '湯婆婆' if ctx.author == target else f'<@{ctx.author.id}>'
    old_name = target.display_name
    new_name = _new_name if _new_name else random.choice(old_name)
    await target.edit(nick=new_name)
    await ctx.send(f"{yubaba}「フン。{old_name}というのかい。贅沢な名だねぇ。\n"
        f"今からお前の名前は{new_name}だ。いいかい、{new_name}だよ。分かったら返事をするんだ、<@{target.id}>!!」")

@nick.error
@ybb.error
async def info_error(ctx: commands.Context, error: Exception):
    await ctx.send(str(error))

@bot.event
async def on_ready():
    print("ready")

bot.run(TOKEN)
