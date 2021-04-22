from discord.ext import commands
import os
import traceback
import random

bot = commands.Bot(command_prefix='m/')
token = os.environ['DISCORD_BOT_TOKEN']
client = discord.Client()

@bot.event
async def on_command_error(ctx, error):
    orig_error = getattr(error, "original", error)
    error_msg = 'エラーが発生しました。'.join(traceback.TracebackException.from_exception(orig_error).format())
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
async def info(ctx):
    embed = discord.Embed(
                          title="murAさんぼっと用info",
                          color=0xFF0000,
                          description="困った時に見るコマンド集。"
                          )
    embed.add_field(name="テスト",value="テスト",inline=False)
    embed.set_footer(text="made by mco2.sys")
    
    await ctx.send(embed=info)


bot.run(token)
