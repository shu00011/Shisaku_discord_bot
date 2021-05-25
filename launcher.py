from discord.ext import commands
import config
import discord

client = discord.Client()
bot = commands.Bot(command_prefix="!")

@bot.event
async def on_ready():
    print("on_ready")

@bot.event
async def on_message(message):
    await bot.process_commands(message) # この文は全プログラム中ここに1つだけ書いておく．そうじゃないと複数回同じ作業を行ったりと異常な動作をする．

bot.load_extension("cogs.event")

bot.load_extension("cogs.commands")

bot.run(config.TOKEN)  # このトークンは外に漏れたらあかん