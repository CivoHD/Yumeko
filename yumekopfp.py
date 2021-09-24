import random
import discord
import asyncio
from discord import colour
from discord import embeds
from discord.ext import commands
from discord.ext.commands.core import command

yumeko_pfp = ['https://64.media.tumblr.com/ab223cf7c9bb4fd5485ae59962370468/fa1036ce56ee4001-8b/s640x960/352a0be1e6dd9fa393706b2384748a289bb5f667.png','https://i.pinimg.com/originals/5a/30/70/5a307054c21e49dd4ac4c3581c551a74.png','https://i.pinimg.com/originals/1f/70/09/1f70091388105b8b8ba631ce3dd535ef.jpg','https://64.media.tumblr.com/702c4f045f1a7deb6b033dbd906b0613/tumblr_otyvg25qyg1vy2tgqo1_250.jpg','https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSrgUMTKYU6rW9N-TD4NHjqru139ZS-wIEM9bW9pXiGQsFAsvz2h3RZfQf6uhx8htGWyOg&usqp=CAU','https://s11.favim.com/orig/7/769/7691/76919/yumeko-jabami-japanese-kakegurui-Favim.com-7691972.jpg','https://i.pinimg.com/originals/66/47/e2/6647e2ac9b0ef3157b069ec261cc052d.jpg','https://i.pinimg.com/originals/4e/a3/a5/4ea3a50ba3d7e11f3321de7881d1aeed.jpg','https://i.pinimg.com/originals/8b/e6/06/8be6068e5886aaaca8b702f0f892154b.jpg','https://i1.wp.com/64.media.tumblr.com/590f1504dc9a77119fd308a061cb6f92/5dc674e75669b9b2-32/s640x960/eaabbd4a1acb359c6d31eb1f0af838a2f81bf040.png','https://64.media.tumblr.com/4eaa791a38b4614b1f25763b57080132/9540ecf27f6a0619-95/s640x960/66904e56cfbd741e92f83c30d08ba6f0caa6e07e.jpg','https://64.media.tumblr.com/250f6eb1ce15c23c797bb9c988f10fbf/66b695ae06990728-af/s500x750/9361a26ef7122eab58528e3d79f5274bc47f5d56.jpg','https://cutewallpaper.org/22/yumeko-icon-wallpapers/2568916634.jpg','https://1tb.favim.com/preview/7/794/7941/79417/7941753.png','https://data.whicdn.com/images/348439521/original.jpg','https://cdn141.picsart.com/324363197188211.png','https://i.pinimg.com/originals/ed/4c/92/ed4c92c09500d27626e793daf7d07f14.png','https://static.wikia.nocookie.net/1a90b0ba-f8be-4aac-8874-f27769323a31/scale-to-width/755','http://pm1.narvii.com/6563/0ec6192da24ff3ef53b2997b94766ff99be11fc2_00.jpg','https://i.imgur.com/YFGU3eT.jpg','https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTN4p5PYIc6g51LwiryPADVANtdUUmk7EwSIA&usqp=CAU','https://data.whicdn.com/images/341684201/original.jpg','https://i0.wp.com/64.media.tumblr.com/54b0aa2cae3a83f31ccc45725134d8e5/982d2f2de7aa877f-f4/s500x750/0cbc21be7474928628b0d4624bb16aa4fdba2674.jpg','https://pbs.twimg.com/media/Els9XUnVgAACVUo.jpg','https://i.pinimg.com/736x/88/2b/f3/882bf31057e166f1774974b8cb439a93.jpg','https://data.whicdn.com/images/342823577/original.jpg','https://lh5.googleusercontent.com/proxy/xk_CinQx-so-zkS37i99fOB8T4SQQSv50Qk02DHClzxH2vQMJlJ3daiTDCIQtgB6EAzE7yLtrSPcEDIDugS1hXwd9MCp8wkJ8whV7rFJ=w1200-h630-p-k-no-nu','https://wallpapercave.com/wp/wp9222582.jpg','https://i.imgur.com/hsRkv1M.jpg','https://wallpapercave.com/uwp/uwp895893.jpeg','https://cdn140.picsart.com/337886382028201.jpg','https://64.media.tumblr.com/4644d8f48d401a54e2788cae58a2cec7/f1d70b3730903438-4d/s1280x1920/6764c2fb537d2b8f5eabbdf84c0ac98e9d0ed2d6.jpg','https://wallpapercave.com/wp/wp9222582.jpg','https://i.pinimg.com/originals/09/90/00/0990002646bb2cb0e78d0c0a891da0b9.jpg','https://static.wikia.nocookie.net/0de6d4a0-f5bc-4ac2-a998-26c60f57f437/scale-to-width/755','https://pbs.twimg.com/media/D2ePSfiWsAAeSGv.jpg','https://i.redd.it/2hxrehwi8ke71.jpg','https://i.pinimg.com/474x/d4/a0/37/d4a0376bc537a117d257270b779920d1.jpg']

class yumekoPfp(commands.Cog):
    
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command(name='yumekoPFP', aliases=['pfp', 'pic'])
    async def yumekoPFP(self, ctx: commands.Context):
        embed = discord.Embed(
            colour=discord.Colour(0xEF1841),
        )
        embed.set_image(url=(random.choice(yumeko_pfp)))

        await ctx.send(embed = embed)