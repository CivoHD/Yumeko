import random
import discord
import asyncio
from discord import colour
from discord import embeds
from discord.ext import commands
from discord.ext.commands import bot
from discord.ext.commands.core import command



class talkCommands(commands.Cog):
    
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command()
    async def hello(self, ctx: commands.Context):
        await ctx.send("Hello cutie")

    @commands.command()
    async def ping(self, ctx: commands.Context):
        await ctx.send("Pong!")

    @commands.command()
    async def creator(self, ctx: commands.Context):
        await ctx.send("Jack_#2163 The Furry Killer")

    @commands.command(name='av')
    async def avatar(self, ctx, member : discord.Member = None):

        if member is None:
            member = ctx.author
        
        memberAvatar = member.avatar_url

        avaEmbed = discord.Embed(title = f"{member.name}'s Avatar!", color = ctx.author.color)
        avaEmbed.set_image(url = memberAvatar)

        await ctx.send(embed = avaEmbed)

       

        
        
        