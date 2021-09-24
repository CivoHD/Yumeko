import discord
import random
import asyncio
import datetime
from discord import user
from discord.ext import commands

rate_percentage0 = ['You are 0% Simp!', 'You are 10% Simp!','You are 15% Simp!','You are 23% Simp!', 'You are 25% Simp!','You are 35% Simp!','You are 36% Simp!', 'You are 40% Simp!', 'You are 46% Simp!','You are 50% Simp!','You are 55% Simp!','You are 65% Simp!','You are 69% Simp!','You are 74% Simp!','You are 87% Simp!','You are 100% Simp!']

rate_percentage1 = ['You are 0% Waifu!', 'You are 10% Waifu!','You are 15% Waifu!','You are 23% Waifu!', 'You are 25% Waifu!','You are 35% Waifu!','You are 36% Waifu!', 'You are 40% Waifu!', 'You are 46% Waifu!','You are 50% Waifu!','You are 55% Waifu!','You are 65% Waifu!','You are 69% Waifu!','You are 74% Waifu!','You are 87% Waifu!','You are 100% Waifu!']

rate_percentage2 = ['You are 0% Gay!', 'You are 10% Gay!','You are 15% Gay!','You are 23% Gay!', 'You are 25% Gay!','You are 35% Gay!','You are 36% Gay!', 'You are 40%Gay!', 'You are 46% Gay!','You are 50% Gay!','You are 55% Gay!','You are 65% Gay!','You are 69% Gay!','You are 74% Gay!','You are 87% Gay!','You are 100% Gay!']

gif = ['https://c.tenor.com/UFvgOBbbTLkAAAAM/happy-anime.gif','https://thumbs.gfycat.com/ActiveArtisticGalapagostortoise-size_restricted.gif','https://www.icegif.com/wp-content/uploads/anime-icegif-15.gif','https://c.tenor.com/WU4iBeEeK88AAAAM/anime-excited.gif','https://c.tenor.com/fRc7yQ0tzFQAAAAM/anime-girl.gif''https://c.tenor.com/6MsukwHKJ58AAAAM/ara-anime.gif','https://c.tenor.com/mKTS5nbF1zcAAAAM/cute-anime-dancing.gif','https://media1.giphy.com/media/a6pzK009rlCak/200.gif','https://static.wikia.nocookie.net/dd4e1d1a-8861-480f-93d8-ccf4d3f96cfc','https://cdn2.scratch.mit.edu/get_image/gallery/26033238_170x100.png']


class yumekoRate(commands.Cog):

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command()
    async def simprate(ctx, message):
   
     value = random.randint(0, 100)
    
     if value > 0:
         
        embed = discord.Embed(colour=0xc81f9f,
                    description=f"{random.choice(rate_percentage0)} {message.author.mention}",
                   
                )
        embed.set_image(url=random.choice(gif))

        await message.channel.send(embed=embed) 



    @commands.command()
    async def waifurate(ctx, message):
   
     value = random.randint(0, 100)
    
     if value > 0:
         
        embed = discord.Embed(colour=0xc81f9f,
                    description=f"{random.choice(rate_percentage1)} {message.author.mention}",
                   
                )
        embed.set_image(url=random.choice(gif))


        await message.channel.send(embed=embed) 

    @commands.command()
    async def gayrate(ctx, message):
   
     value = random.randint(0, 100)
    
     if value > 0:
         
        embed = discord.Embed(colour=0xc81f9f,
                    description=f"{random.choice(rate_percentage2)} {message.author.mention}",
                   
                )
        embed.set_image(url=random.choice(gif))


        await message.channel.send(embed=embed) 
