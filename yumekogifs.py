import random
import discord
import asyncio
from discord import colour
from discord import embeds
from discord.ext import commands
from discord.ext.commands.core import command

yumeko_gifs = ['https://c.tenor.com/gqgd15rUhN8AAAAC/yes.gif','https://c.tenor.com/P6g2p9Cm_cEAAAAC/kakeuguri-yumiko.gif','https://c.tenor.com/gqgd15rUhN8AAAAC/yes.gif','https://c.tenor.com/MncEUTptFd0AAAAC/yumeko-jabami.gif','https://c.tenor.com/6k-wG_Ql8XEAAAAM/yumeko.gif','https://c.tenor.com/UMe4nzNj4j8AAAAC/anime-kakegurui.gif','https://c.tenor.com/cCU63bbIfIwAAAAM/rage-red.gif','https://c.tenor.com/LgBWQk5HuSkAAAAC/kakegurui-look-up.gif','https://c.tenor.com/0-jPoQloNcMAAAAM/yumeko-jabami-%E8%9B%87%E5%96%B0.gif','https://c.tenor.com/FtGC9ZiflYgAAAAC/yumeko-jabami-%E8%9B%87%E5%96%B0.gif','https://c.tenor.com/dTNRs-1GEccAAAAC/yumeko-yumeko-jabami.gif','https://c.tenor.com/lI40FV_QFNgAAAAM/yumeko.gif','https://c.tenor.com/H9mdtA_FGmAAAAAC/yumeko-jabami.gif','https://c.tenor.com/dTNRs-1GEccAAAAC/yumeko-yumeko-jabami.gif','https://c.tenor.com/mniEa3laMLIAAAAM/yumeko-iku.gif','https://c.tenor.com/dITaRjCMNowAAAAC/yumeko-jabami.gif','https://c.tenor.com/_e9dBLsrjnMAAAAd/yumeko-jabami-yumeko.gif','https://c.tenor.com/tGMqgl8SScAAAAAC/jvson.gif','https://c.tenor.com/SjXvXsMHUcgAAAAC/jvson.gif']
yumeko_talk = ['https://c.tenor.com/SMyLWBG8a9sAAAAC/kakegurui-anime.gif','https://c.tenor.com/Csshcuv9swEAAAAM/anime-love-kakegurui.gif','https://c.tenor.com/nFkt7_hhDfAAAAAM/yumeko-jabami-eyes.gif','https://c.tenor.com/u7rmZJIlfosAAAAC/kakegurui-mary-saotome.gif','https://c.tenor.com/wb1JbRtknhgAAAAC/kakegurui-momobami-kirari.gif','https://c.tenor.com/TqWZ9Q6JiZIAAAAC/qtlixi-yumeko.gif','https://c.tenor.com/bgf9C1TAV5AAAAAC/yumeko.gif','https://c.tenor.com/NLLUs1-KdSEAAAAC/kakeuguri-yumiko.gif','https://c.tenor.com/6bWp8WRMR18AAAAC/yumeko-jabami.gif','https://c.tenor.com/-gQ-EL9EtAcAAAAM/yumeko-yumeko-jabami.gif','https://c.tenor.com/9flScK2tW7kAAAAC/yumeko-jabami-mary-saotome.gif','https://c.tenor.com/pzygTZSmzqIAAAAM/yumeko-neko-mimi.gif','https://c.tenor.com/JrIQN4iOblsAAAAC/yumeko-jabami.gif','https://c.tenor.com/uK2wDmgtqpUAAAAM/kakegurui-smiling.gif','I don’t know if you’re a good gambler, but you’re the lowest of the low as a person.','I dislike situations where I know for sure If I’m going to win or lose. Because it’s not really gambling','I want to gamble more and more!','Doubt, anger, despair, you must feel as if you could scream,. am I right?','You won’t be able to fool anyone if you’re not prepared to shed your own blood.','Friends assist each other in times of need, do they not?','This doesn’t stop within the walls of a casino, or it’s cash flow.','The amount of money one owns ultimately decides the victor.','The larger the ambition the greater the risk.','To make your ambitions come true, you have to take risks.','Business owners put up collateral to borrow money.','Pro-athletes give up their teenage years to train.','If you want to earn something, you need to reach out for it.','The only one who can decide your worth.. is you.']


class yumekoGifs(commands.Cog):
    
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command(name='yumeko', aliases=['gif', 'waifu', 'senpai'])
    async def yumeko(self, ctx: commands.Context):
        embed = discord.Embed(
            title=(random.choice(yumeko_talk)),
            colour=discord.Colour(0xEF1841),
        )
        embed.set_image(url=(random.choice(yumeko_gifs)))

        await ctx.send(embed = embed)