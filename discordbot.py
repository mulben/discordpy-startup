from discord.ext import commands
import os
import traceback
import random

bot = commands.Bot(command_prefix='m/')
token = os.environ['DISCORD_BOT_TOKEN']


@bot.event
async def on_command_error(ctx, error):
    orig_error = getattr(error, "original", error)
    error_msg = ''.join(traceback.TracebackException.from_exception(orig_error).format())
    await ctx.send(error_msg)


@bot.command(name='ping')
async def ping(ctx):
    await ctx.send('pong!!')
@bot.command(name='ネタ')
async def _neta(ctx):
    await ctx.reply('あたいったら最強ね')
@bot.command(name='ネタ2')
async def _neta2(ctx):
    await ctx.reply('不死鳥の名は伊達じゃない by 響')
@bot.command(name='公式サイト')
async def site(ctx):
    await ctx.send('http://yugiri.starfree.jp/index.html')
@bot.command(name="info")
async def discord_help(ctx):
    colour = random.randint(0x000000, 0xffffff)
    embed = discord.Embed(title="info", description="murAさんぼっとのinformationです。困った時はこれを確認。",url="URL", colour=colour)
    embed.set_thumbnail(url=bot.user.avatar_url_as(format='png'))
    await ctx.reply(embed=embed)



bot.run(token)
