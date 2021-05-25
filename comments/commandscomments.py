from discord.ext import commands
import asyncio
import discord
import datetime
import random

class Commands(commands.Cog):
    def __init__(self,bot):
        self.bot=bot

    @commands.command()
    async def morning(self,ctx):   # ctxはコマンドを定義する上で必須の引数．コマンドの実行に関する情報を保持．
        random_contents=[
            "鮭ごはん",
            "鮭おにぎり",
            "鮭茶漬け"
        ]
        content=random.choice(random_contents)
        await ctx.send(f"おはようございます，{ctx.author.name}さん！")
        await ctx.send(f"僕の朝ごはんは{content}です！")
        await ctx.send(f"{content}って美味しいですよね！")

    @commands.command()
    async def now(self,ctx):
        #Embed（埋め込みテキスト）インスタンスを生成
        embed = discord.Embed()
    #Embedの表示色を指定
        embed.color = discord.Color.dark_grey()

        thistime =datetime.datetime.now()
        tstr = thistime.strftime('%Y/%m/%d/%H:%M')
        embed.add_field(name="現在時刻",value=tstr)
        await ctx.send(embed=embed)

    @commands.command()
    async def weekday(self,ctx):
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

    @commands.command()
    async def DM(self,ctx, member: discord.Member, content):
    #Embed（埋め込みテキスト）インスタンスを生成
        embed = discord.Embed()
    #Embedの表示色を指定
        embed.color = discord.Color.dark_grey()

        embed.add_field(name=f"{member.name}にDMを送信．",value="成功．")
        await ctx.send(embed=embed)
        await member.send(content=content)

    @commands.command()
    async def client_play(self,ctx, title):
        client = self.bot
        game = discord.Game(name=title)

    #Embed（埋め込みテキスト）インスタンスを生成
        embed = discord.Embed()
    #Embedの表示色を指定
        embed.color = discord.Color.dark_grey()

        embed.add_field(name=f"試作botがプレイしているのは",value=title)
        await ctx.send(embed=embed)

        await client.change_presence(activity=game)

    @commands.command()
    async def typing(self,ctx):
        embed = discord.Embed()
    #Embedの表示色を指定
        embed.color = discord.Color.dark_grey()

        embed.add_field(name="typing now",value="...")
        await ctx.send(embed=embed)
        async with ctx.channel.typing():
        # 長い処理の代わりにsleepする
            await asyncio.sleep(3)

    @commands.command()
    async def invite(self,ctx):
    # 24時間有効，10人まで招待かのうな招待を作成
        channel = ctx.channel
        invite = await channel.create_invite(max_age=3600 * 24, max_users=10)
        await ctx.send(invite.url)

    @commands.command()
    async def icon(self,ctx):
        await ctx.send(file=discord.File(fp="icon.JPG"))

def setup(bot):
    bot.add_cog(Commands(bot))