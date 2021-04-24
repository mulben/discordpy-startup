from discord.ext import commands
import os
import traceback
import random
import discord

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
async def info(ctx):
    embed = discord.Embed(
                          title="murAさんぼっと用info",
                          color=0x3498db,
                          description="困った時に見るコマンド集。"
                          )
    embed.add_field(name="ネタ",value="Botが動いているか確認するためのテスト用コマンドです。",inline=False)
    embed.add_field(name="ネタ2",value="上と同じです。",inline=False)
    embed.add_field(name="公式サイト",value="音楽と絵文字の部屋の公式サイトのリンクが表示されます。未完成です。",inline=False)
    embed.add_field(name="info",value="困ったときに使うと、これが表示されます。",inline=False)
    embed.set_footer(text="made by mco2.sys")
    await ctx.send(embed=embed)

bot.run(token)
