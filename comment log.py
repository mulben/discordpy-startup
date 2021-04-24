from discord.ext import commands
import os
import traceback
import random
import discord
import re

bot = commands.Bot(command_prefix='m/')
token = os.environ['DISCORD_BOT_TOKEN']
ch_id = 835407208740159500
channel = bot.get_channel(ch_id)


@bot.event
async def on_command_error(ctx, error):
    orig_error = getattr(error, "original", error)
    error_msg = ''.join(traceback.TracebackException.from_exception(orig_error).format())
    await ctx.send(error_msg)

@bot.event
async def on_message(message):
    if message.author.bot:
        return
    
    if re.match(r".*", message.content):
        msg = f'{message.channel.id}で{message.author.name}さんが発言しました'
        await bot.get_channel(ch_id).send(msg)
        
bot.run(token)
