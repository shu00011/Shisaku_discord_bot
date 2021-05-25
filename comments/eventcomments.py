from discord.ext import commands

class Event(commands.Cog):
    def __init__(self,bot):
        self.bot=bot

    @commands.Cog.listener()
    async def on_message(self,message):  # on_message() メッセージ（テキストチャンネルへの投稿）が発生したことを通知するイベント．イベントリスナー．イベントリスナーは必ずコルーチン関数で定義する必要がある．
        if message.author == self.bot.user:
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

# 以下未テスト．

    @commands.Cog.listener()
    async def on_guild_join(self,guild):
    # 新しくGuildに入ったらログを残す．
        print(f"はじめまして！僕は「{self.bot.user.name}」です！よろしくね！")

    @commands.Cog.listener()
    async def on_member_join(self,member):
    # Guildメンバーが増えたら挨拶DMを送信．
    # memberのDM受け取り設定によっては失敗する．
        await member.channel.send(
            f"{member.name}さん，サーバー「{member.guild.name}」にようこそ！\n"
            f"僕は「{self.bot.user.name}です！よろしくね！"
        )

def setup(bot):
    bot.add_cog(Event(bot))