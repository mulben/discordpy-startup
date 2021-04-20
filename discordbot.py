from discord.ext import commands
import os
import traceback

bot = commands.Bot(command_prefix='/')
token = os.environ['DISCORD_BOT_TOKEN']


@bot.event
async def on_command_error(ctx, error):
    orig_error = getattr(error, "original", error)
    error_msg = ''.join(traceback.TracebackException.from_exception(orig_error).format())
    await ctx.send(error_msg)
    async def on_ready():
    await bot.change_presence(activity=discord.Game(f"Herokuを")

@bot.command()
async def ping(ctx):
    await ctx.send('pong')
if message.content == 'akiさん':
        await message.channel.send('なに？','(  ᐛ)ﾊﾞﾅﾅ','引きちぎるぞ','伸ばすぞ','ねじる','( ᐛ )','(￣･ω･￣)','( 'ω'ｱﾋﾞｬｰ')


bot.run(token)
