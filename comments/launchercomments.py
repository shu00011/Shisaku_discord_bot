from discord.ext import commands
import config
import discord

client = discord.Client()   # Discordサーバとの接続やBot自身に関する機能を持つクラス．BotクラスはClientクラスを継承するため，Clientとして扱える．
bot = commands.Bot(command_prefix="!")
# Botというクラスのインスタンスを生成し，botという名前の変数に格納．
# "!"はプレフィックス．

@bot.event  # デコレーター．botにready eventが発生したときの処理の定義．ここで定義した処理はBotがDiscord APIサーバに接続詞，Botの動作に必要なデータ取得が完了したときに実行される．
async def on_ready():   #async def コルーチン関数定義
    print("on_ready")   # 標準出力（通常はターミナル上）に出力する

@bot.event
async def on_message(message):
 # @bot.command()によるコマンド定義と，on_message()イベントリスナーの定義を同時に使用する際に必要．
    await bot.process_commands(message) # この文は全プログラム中ここに1つだけ書いておく．そうじゃないと複数回同じ作業を行ったりと異常な動作をする．

bot.load_extension("cogs.event")

bot.load_extension("cogs.commands")

bot.run(config.TOKEN)  # このトークンは外に漏れたらあかん
# botのrunメソッドにトークンを引数として渡すとDiscord APIサーバへの接続を開始し，Botアカウントにログインする．
# 本来はソースコードに直接トークンを記載するのは避けるべき．

# コルーチン関数とは待ち時間の発生するような処理を実施する際にその関数の実行を中断し，その完了を待つ間に別の処理を実施することで効率的にプログラムを動作させる仕組みをもつ関数のこと．

# Cogsとは複数のイベントリスナーやコマンドを1つのクラスにまとめることができる機能のこと．
# ExtensionはBotの動作を留めることなく動的にモジュールを再度読み込むための仕組み．