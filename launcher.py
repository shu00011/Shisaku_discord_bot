from discord.ext import commands
import config

bot = commands.Bot(command_prefix="!")
# Botというクラスのインスタンスを生成し，botという名前の変数に格納．

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

    if "おはよう" in message.content:    # "Bot"に反応
        await message.channel.send("おはよう！")

    if "おやすみ" in message.content:    # "Bot"に反応
        await message.channel.send("おやすみー！")

    if "はろー" in message.content:    # "Bot"に反応
        await message.channel.send("Hello, World!")

    if "ハロー" in message.content:    # "Bot"に反応
        await message.channel.send("Hello, World!")

    if "hello" in message.content:    # "Bot"に反応
        await message.channel.send("Hello, World!")

    if "Hello" in message.content:    # "Bot"に反応
        await message.channel.send("Hello, World!")

@bot.event
async def on_guild_join(guild):
    # 新しくGuildに入ったらログを残す．
    print(f"はじめまして！僕は「{bot.user.name}」です！よろしくね！")

@bot.event
async def on_member_join(member):
    # Guildメンバーが増えたら挨拶DMを送信．
    # memberのDM受け取り設定によっては失敗する．
    await member.channnel.send(
        f"{member.name}さん，サーバー「{member.guild.name}」にようこそ！\n"
        f"僕は「{bot.user.name}です！よろしくね！"
    )

bot.run(config.TOKEN)  # このトークンは外に漏れたらあかん
# botのrunメソッドにトークンを引数として渡すとDiscord APIサーバへの接続を開始し，Botアカウントにログインする．
# 本来はソースコードに直接トークンを記載するのは避けるべき．

# コルーチン関数とは待ち時間の発生するような処理を実施する際にその関数の実行を中断し，その完了を待つ間に別の処理を実施することで効率的にプログラムを動作させる仕組みをもつ関数のこと．