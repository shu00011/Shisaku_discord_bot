from discord.ext import commands
import asyncio
import discord
import datetime
import random

class Commands(commands.Cog):
    def __init__(self,bot):
        self.bot=bot

    @commands.command()
    async def morning(self,ctx):
        random_contents=[
            "しろごはん",
            "ぎんしゃり",
            "鮭茶漬け"
        ]
        content=random.choice(random_contents)
        await ctx.send(f"おはようございます，{ctx.author.name}さん！")
        await ctx.send(f"僕の朝ごはんは{content}です！")
        await ctx.send(f"{content}って美味しいですよね！")

    @commands.command()
    async def weekday(self,ctx):
        embed = discord.Embed()
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
        embed = discord.Embed()
        embed.color = discord.Color.dark_grey()

        embed.add_field(name=f"{member.name}にDMを送信．",value="成功．")
        await ctx.send(embed=embed)
        await member.send(content=content)

    @commands.command()
    async def client_play(self,ctx, title):
        client = self.bot
        game = discord.Game(name=title)

        embed = discord.Embed()
        embed.color = discord.Color.dark_grey()

        embed.add_field(name="試作botがプレイしているのは",value=title)
        await ctx.send(embed=embed)

        await client.change_presence(activity=game)

    @commands.command()
    async def typing(self,ctx):
        embed = discord.Embed()
        embed.color = discord.Color.dark_grey()

        embed.add_field(name="typing now",value="...")
        await ctx.send(embed=embed)
        async with ctx.channel.typing():
            await asyncio.sleep(3)

    @commands.command()
    async def invite(self,ctx):
        channel = ctx.channel
        invite = await channel.create_invite(max_age=3600 * 24, max_users=10)
        await ctx.send(invite.url)

    @commands.command()
    async def icon(self,ctx):
        await ctx.send(file=discord.File(fp="icon.JPG"))

    @commands.command()
    async def help_b(self,ctx):
        embed = discord.Embed(title="試作bot help")
        embed.color = discord.Color.dark_grey()

        embed.add_field(name="1.挨拶をすると挨拶を返してくれます．",
            value="(ex. 「おはよう」「おやすみ」「はろー」「ハロー」「Hello」「hello」)\n他に，「Bot」にも反応します．", inline = False)
        embed.add_field(name="2.\"!\"を先頭につけるとコマンドになります．",
            value="!help_b: 本helpを表示．\n!morning: botの当日の朝ごはんを表示．\n!weekday: 当日の曜日を表示．\n!DM <memberName> <text>: <memberName>のDMに<text>を送信．\n!client_play <title>: 試作botを<title>をプレイ中にする．\n!typing: 試作botがtypingする．\n!invite: 招待を作成．(24h有効，最大10人まで)\n!icon: 試作botのicon画像を表示． ",
            inline=False)
        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(Commands(bot))
