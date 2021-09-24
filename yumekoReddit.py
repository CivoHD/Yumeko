import random
import praw
import discord
import asyncio
from discord import colour
from discord import embeds
from discord.ext import commands
from discord.ext.commands.core import command

reddit = praw.Reddit(client_id = "8YuC0y5bz7XIMT0WSERwZQ",
                     client_secret = "10QRD2g2WVdTx8Mo1r0dKPlzsDiWOg",
                     username = "BotPraw",
                     password = "meme1234",
                     user_agent = "botpraw")

class Reddit(commands.Cog):
    
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command(name='Kakegurui', aliases=['yumekoreddit', 'reddit'])
    async def yumekoreddit(self, ctx: commands.Context):
        subreddit = reddit.subreddit("Kakegurui")
        all_subs = []

        top = subreddit.top(limit = 50)

        for submission in top:
            all_subs.append(submission)
            
        random_sub = random.choice(all_subs)

        name = random_sub.title
        url = random_sub.url

        em = discord.Embed(
            title= name,
            colour=(discord.Colour(0xF13752)),
        )
        em.set_image(url = url)

        await ctx.send(embed = em)