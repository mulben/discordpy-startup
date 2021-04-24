from discord.ext import commands
import os
import traceback
import random
import discord
import re

bot = commands.Bot(command_prefix='m/')
token = os.environ['DISCORD_BOT_TOKEN']
ch_id = 835407208740159500
channel = client.get_channel(ch_id)


@bot.event
async def on_command_error(ctx, error):
    orig_error = getattr(error, "original", error)
    error_msg = ''.join(traceback.TracebackException.from_exception(orig_error).format())
    await ctx.send(error_msg)

@client.event
async def on_message(message):
    if message.author.bot:
        return
    
    if re.match(r".*", message.content):
        msg = f'{message.channel.id}で{message.author.id}_{message.author.name}さんが発言しました'
        await client.get_channel(ch_id).send(msg)
        

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
    

    

@bot.command(name="ui")
async def ui(ctx):
    embed = discord.Embed(
                          title="murAさんぼっとのBot情報",
                          color=0x2ecc71,
                          descroption="Botの詳しい概要です。"
                          )
    embed.add_field(name="```Name```",value="murAさんぼっと",inline=False)
    embed.add_field(name="```Version```",value="1.3.0|Discord.py[voice]1.7.1|Python 3.9.0",inline=False)
    embed.add_field(name="```DevelopLang```",value="Python",inline=False)
    embed.add_field(name="```Server```",value="Heroku-DynoFree[Git push]",inline=False)
    embed.add_field(name="```Made Date```",value="2021/04/10",inline=False)
    embed.set_footer(text="made by mco2.sys #8200")
    await ctx.send(embed=embed)
    
    
@bot.command(name="info")
async def info(ctx):
    embed = discord.Embed(
                          title="murAさんぼっと用info",
                          color=0x3498db,
                          description="困った時に見るコマンド集。"
                          )
    embed.add_field(name="```ネタ```",value="Botが動いているか確認するためのテスト用コマンドです。",inline=False)
    embed.add_field(name="```ネタ2```",value="上と同じです。",inline=False)
    embed.add_field(name="```公式サイト```",value="音楽と絵文字の部屋の公式サイトのリンクが表示されます。未完成です。",inline=False)
    embed.add_field(name="```ui```",value="Botの概要が見れます。",inline=False)
    embed.add_field(name="```info```",value="困ったときに使うと、これが表示されます。",inline=False)
    embed.set_footer(text="made by mco2.sys #8200")
    await ctx.send(embed=embed)

bot.run(token)
