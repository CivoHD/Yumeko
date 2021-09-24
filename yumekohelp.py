import random
import discord
import asyncio
from discord import colour
from discord import embeds
from discord.ext import commands
from discord.ext.commands.core import command



class helpCommand(commands.Cog):
    
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.group(invoke_without_command=True)
    async def help(self, ctx: commands.Context):
        em = discord.Embed(title= 'Help', description= "Use y!help <command> for extended information on a command.",color = ctx.author.color)

        em.add_field(name = "Yumeko Gif's", value = "gifs")
        em.add_field(name = "Yumeko Pfps", value = "pfp")
        em.add_field(name = "Kakegurui Reddit", value = "reddit")
        em.add_field(name = "Yumeko Rates", value = "rates")
        em.add_field(name = "Action Gif's", value = "action")
        em.add_field(name = "Music Commands", value = "music")
        em.add_field(name = "Economy Commands", value = "economy")
        em.add_field(name = "Lots More Coming Soon...", value = "more")

        await ctx.send(embed = em)

    @help.command()
    async def gifs(self, ctx: commands.Context):

        em = discord.Embed(title= 'gifs', description= "Displays a Yumeko Gif.",color = ctx.author.color)

        em.add_field(name = "yumeko gifs", value = "y! yumeko  |  gif")

        await ctx.send(embed = em)

    @help.command()
    async def pfp(self, ctx: commands.Context):

        em = discord.Embed(title= 'pfp', description= "Displays Random Yumeko pfp.",color = ctx.author.color)

        em.add_field(name = "yumeko pfp", value = "y! yumekopfp  |  pfp  |  pic")

        await ctx.send(embed = em)

    @help.command()
    async def rates(self, ctx: commands.Context):

        em = discord.Embed(title= 'simprate', description= "Displays How Much of a Simp You Are To Yumeko." ,color = ctx.author.color)

        em.add_field(name = "Yumeko Simprate", value = "y! simprate  |  gayrate  |  waifurate")

        await ctx.send(embed = em)


    @help.command()
    async def action(self, ctx: commands.Context):

        em = discord.Embed(title= 'action gifs', description= "Displays a action on which you have chosen." ,color = ctx.author.color)

        em.add_field(name = "actions", value = "y! punch  |  poke  |  flick  |  kiss  |  hug  |  kick")

        await ctx.send(embed = em)

    @help.command()
    async def music(self, ctx: commands.Context):

        em = discord.Embed(title= 'music', description= "Music Commands." ,color = ctx.author.color)

        em.add_field(name = "Commands:", value = """
        ◦ y!connect
        ◦ y!disconnect
        ◦ y!play <query>
        ◦ y!skip
        ◦ y!pause
        ◦ y!resume
        ◦ y!seek <seconds> [reverse=False]
        ◦ y!volume <vol> [forced=False]
        ◦ y!loop [type]
        ◦ y!nowplaying
        ◦ y!queue
        ◦ y!equalizer

        """)

        await ctx.send(embed = em)

    @help.command()
    async def economy(self, ctx: commands.Context):

        em = discord.Embed(title= 'economy', description= "Economy Commands." ,color = ctx.author.color)

        em.add_field(name = "Commands:", value = """
        ◦ y!balance
        ◦ y!beg
        ◦ y!withdraw
        ◦ y!deposit
        ◦ y!send
        ◦ y!rob
        ◦ y!slots
        ◦ y!shop
        ◦ y!buy
        ◦ y!bag
        ◦ y!buy this
        ◦ y!sell
        ◦ y!leaderboard

        """)

        await ctx.send(embed = em)


    @help.command()
    async def more(self, ctx: commands.Context):

        em = discord.Embed(title= 'New Fetures', description= "New ideas may be here" ,color = ctx.author.color)

        em.add_field(name = "Waiting...", value = "Waiting more...")

        await ctx.send(embed = em)


    