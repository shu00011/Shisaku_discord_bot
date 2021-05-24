from discord.ext import commands
import config
import asyncio

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

    await bot.process_commands(message) # @bot.command()によるコマンド定義と，on_message()イベントリスナーの定義を同時に使用する際に必要．

@bot.command()
async def juice(ctx):
    # 絵文字の表示
    watermelon ='N{Watermelon}'
    grapes = 'N{Grapes}'
    tangerine = 'N{Tangerine}'
    kiwi = 'N{Kiwifruit}'
    pineapple = 'N{Pineapple}'
    strawberry = 'N{Strawberry}'
    melon = 'N{Melon}'
    banana = 'N{Banana}'

    # wait_forに渡すcheck関数
    def check_reaction(reaction, user):
        # リアクションの送信userを確認
        user_ok = (user == ctx.author)
        # リアクションの種別を確認
        reaction_ok=(reaction.emoji == watermelon or
                     reaction.emoji == grapes or
                     reaction.emoji == tangerine or
                     reaction.emoji == kiwi or
                     reaction.emoji == pineapple or
                     reaction.emoji == strawberry or
                     reaction.emoji == melon or
                     reaction.emoji == banana)
        return user_ok and reaction_ok

    # message送信
    await ctx.send(f"こんにちは，{ctx.author.name}さん！")
    msg = await ctx.send("今日は何のジュースにしますか？")
    # 送信したメッセージにリアクションを付与
    await msg.add_reaction(watermelon)
    await msg.add_reaction(grapes)
    await msg.add_reaction(tangerine)
    await msg.add_reaction(kiwi)
    await msg.add_reaction(pineapple)
    await msg.add_reaction(strawberry)
    await msg.add_reaction(melon)
    await msg.add_reaction(banana)
    # ユーザからのリアクションを待つ
    reaction, user = await bot.wait_for("reaction_add", check=check_reaction)
    # ユーザのリアクションに応じてメッセージを変える
    if reaction.emoji == watermelon:
        flavor = "スイカ"
    elif reaction.emoji == grapes:
        flavor = "ぶどう"
    elif reaction.emoji == tangerine:
        flavor = "みかん"
    elif reaction.emoji == kiwi:
        flavor = "キウイ"
    elif reaction.emoji == pineapple:
        flavor = "マンゴーパイン"
    elif reaction.emoji == strawberry:
        flavor = "イチゴミルク"
    elif reaction.emoji == melon:
        flavor = "タカミメロン"
    else:
        flavor = "バナナミルク"

    await ctx.send(f"今日のジュースは{flavor}ジュースですね！")


@bot.command()
async def morning(ctx):   # ctxはコマンドを定義する上で必須の引数．コマンドの実行に関する情報を保持．
    # 待機するメッセージのチェック関数
    def check_message_author(msg):
        return msg.author is ctx.author

    await ctx.send(f"おはようございます，{ctx.author.name}さん！")
    await ctx.send("今日の朝ごはんは何ですか？")
    # チェック関数に合格するようなメッセージを待つ
    try:
        msg = await bot.wait_for('message', check=check_message_author, timeout=10) # 秒数．例外が発生するとexceptへ．
    except asyncio.TimeoutError:
        await ctx.send("タイムアウト．")
        return
    # 受け取ったメッセージの内容を使って返信
    await ctx.send(f"今日の朝ごはんは「{msg.content}」なんですね！")

@bot.command()
async def guild_info(ctx):
    guild = ctx.guild   # guildインスタンスの取得
    await ctx.send(
        f"サーバ名：{guild.name}\n"
        f"サーバID：{guild.id}\n"
        f"サーバオーナー：{guild.owner.name}\n"
        f"メンバー数：{guild.member_count}\n"
        f"作成日：{guild.created_at+datetime.timedelta(hours=9)}\n"
    )

@bot.command()
async def guild_create_channel(ctx, name):
    guild = ctx.guild
    await guild.create_text_channel(name=name)
    await ctx.send(f"テキストチャンネル{name}を作成しました．")

@bot.command()  # 反応はしたが取得できず．
async def mobile(ctx):
    member = ctx.author
    await ctx.send(
        f"status:{str(member.status)}\n"
        f"mobileからのログインか？:{member.is_on_mobile()}"
    )

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