from discord.ext import commands
import os
import traceback

bot = commands.Bot(command_prefix='m/')
token = os.environ['DISCORD_BOT_TOKEN']


@bot.event
async def on_command_error(ctx, error):
    orig_error = getattr(error, "original", error)
    error_msg = ''.join(traceback.TracebackException.from_exception(orig_error).format())
    await ctx.send(error_msg)

@bot.command(name='ping')
async def ping(ctx):
    await ctx.send('pong')
@bot.command(name='ネタ')
async def _neta(ctx):
    await ctx.reply('あたいったら最強ね')



bot.run(token)
