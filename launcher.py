from discord.ext import commands
import config
import asyncio
import discord
import datetime

client = discord.Client()   # Discordサーバとの接続やBot自身に関する機能を持つクラス．BotクラスはClientクラスを継承するため，Clientとして扱える．
bot = commands.Bot(command_prefix="!")
# Botというクラスのインスタンスを生成し，botという名前の変数に格納．
# "!"はプレフィックス．

@bot.event  # デコレーター．botにready eventが発生したときの処理の定義．ここで定義した処理はBotがDiscord APIサーバに接続詞，Botの動作に必要なデータ取得が完了したときに実行される．
async def on_ready():   #async def コルーチン関数定義
    print("on_ready")   # 標準出力（通常はターミナル上）に出力する

@bot.event
async def on_message(message):  # on_message() メッセージ（テキストチャンネルへの投稿）が発生したことを通知するイベント．イベントリスナー．イベントリスナーは必ずコルーチン関数で定義する必要がある．
    if message.author == bot.user:
        # botからのメッセージには反応しないよう判定．これがないと無限ループになるから．
        return

    if "Bot" in message.content:    # "Bot"に反応
        await message.channel.send("はい，Botです！")

    if "おはよう" in message.content:
        await message.channel.send("おはよう！")

    if "おやすみ" in message.content:
        await message.channel.send("おやすみー！")

    if "はろー" in message.content:
        await message.channel.send("Hello, World!")

    if "ハロー" in message.content:
        await message.channel.send("Hello, World!")

    if "hello" in message.content:
        await message.channel.send("Hello, World!")

    if "Hello" in message.content:
        await message.channel.send("Hello, World!")

    await bot.process_commands(message) # @bot.command()によるコマンド定義と，on_message()イベントリスナーの定義を同時に使用する際に必要．

@bot.command()
async def morning(ctx):   # ctxはコマンドを定義する上で必須の引数．コマンドの実行に関する情報を保持．
    await ctx.send(f"おはようございます，{ctx.author.name}さん！")
    await ctx.send("僕の朝ごはんは鮭おにぎりです！")
    await ctx.send("鮭おにぎりって美味しいですよね！")

@bot.command()
async def now(ctx):
    #Embed（埋め込みテキスト）インスタンスを生成
    embed = discord.Embed()
    #Embedの表示色を指定
    embed.color = discord.Color.dark_grey()

    thistime =datetime.datetime.now()
    tstr = thistime.strftime('%Y/%m/%d/%H:%M')
    embed.add_field(name="現在時刻",value=tstr)
    await ctx.send(embed=embed)

@bot.command()
async def weekday(ctx):
    #Embed（埋め込みテキスト）インスタンスを生成
    embed = discord.Embed()
    #Embedの表示色を指定
    embed.color = discord.Color.dark_grey()

    thistime =datetime.datetime.now()
    wday = thistime.weekday()

    if wday == 0:
        weday = "月曜日"
    elif wday == 1:
        weday = "火曜日"
    elif wday == 2:
        weday = "水曜日"
    elif wday == 3:
        weday = "木曜日"
    elif wday == 4:
        weday = "金曜日"
    elif wday == 5:
        weday = "土曜日"
    else:
        weday = "日曜日"

    embed.add_field(name="本日の曜日",value=weday)
    await ctx.send(embed=embed)

@bot.command()
async def DM(ctx, member: discord.Member, content):
    #Embed（埋め込みテキスト）インスタンスを生成
    embed = discord.Embed()
    #Embedの表示色を指定
    embed.color = discord.Color.dark_grey()

    embed.add_field(name=f"{member.name}にDMを送信．",value="成功．")
    await ctx.send(embed=embed)
    await member.send(content=content)

@bot.command()
async def client_play(ctx, title):
    client = bot
    game = discord.Game(name=title)

    #Embed（埋め込みテキスト）インスタンスを生成
    embed = discord.Embed()
    #Embedの表示色を指定
    embed.color = discord.Color.dark_grey()

    embed.add_field(name=f"試作botがプレイしているのは",value=title)
    await ctx.send(embed=embed)

    await client.change_presence(activity=game)

@bot.command()
async def typing(ctx):
    embed = discord.Embed()
    #Embedの表示色を指定
    embed.color = discord.Color.dark_grey()

    embed.add_field(name="typing now",value="...")
    await ctx.send(embed=embed)
    async with ctx.channel.typing():
        # 長い処理の代わりにsleepする
        await asyncio.sleep(3)

@bot.command()
async def invite(ctx):
    # 24時間有効，10人まで招待かのうな招待を作成
    channel = ctx.channel
    invite = await channel.create_invite(max_age=3600 * 24, max_users=10)
    await ctx.send(invite.url)

@bot.command()
async def icon(ctx):
    await ctx.send(file=discord.File(fp="icon.JPG"))

# 以下未テスト．

@bot.event
async def on_guild_join(guild):
    # 新しくGuildに入ったらログを残す．
    print(f"はじめまして！僕は「{bot.user.name}」です！よろしくね！")

@bot.event
async def on_member_join(member):
    # Guildメンバーが増えたら挨拶DMを送信．
    # memberのDM受け取り設定によっては失敗する．
    await member.channel.send(
        f"{member.name}さん，サーバー「{member.guild.name}」にようこそ！\n"
        f"僕は「{bot.user.name}です！よろしくね！"
    )

bot.run(config.TOKEN)  # このトークンは外に漏れたらあかん
# botのrunメソッドにトークンを引数として渡すとDiscord APIサーバへの接続を開始し，Botアカウントにログインする．
# 本来はソースコードに直接トークンを記載するのは避けるべき．

# コルーチン関数とは待ち時間の発生するような処理を実施する際にその関数の実行を中断し，その完了を待つ間に別の処理を実施することで効率的にプログラムを動作させる仕組みをもつ関数のこと．