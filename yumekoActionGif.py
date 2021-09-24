import random
import discord
import asyncio
from discord import colour
from discord import embeds
from discord.ext import commands
from discord.ext.commands.core import command


punching_gifs = ["https://c.tenor.com/b9aXVS6p7ucAAAAC/edens-zero-shiki-granbell.gif","https://i.imgur.com/g91XPGA.gif","https://i.imgur.com/7jErgl1.gif","https://i.imgur.com/hlqNBXp.gif","https://i.imgur.com/jznCcr2.gif","https://i.imgur.com/f2kkp3L.gif", "https://i.imgur.com/cgMbUYX.gif", "https://i.imgur.com/pX1E9uU.gif", "https://i.imgur.com/hODM1tI.gif", "https://i.imgur.com/e4bi40y.gif"]
punching_names = ['Knocks You Out!', 'Punches You!', 'Destroys Your Skull!']

poke_gifs = ["https://c.tenor.com/NjIdfk7i3bsAAAAC/poke-poke-poke.gif","https://c.tenor.com/cEZZ8LBsNVcAAAAC/saikava-dragon.gif","https://c.tenor.com/Uy90Hf8peO8AAAAC/testament-of-sister-new-devil-shinmai-maou-no-testament.gif","https://c.tenor.com/ZmSzg7S4HukAAAAC/annoyed-info-chan.gif","https://c.tenor.com/HPlp78w2otYAAAAC/poke-anime.gif","https://c.tenor.com/1YMrMsCtxLQAAAAM/anime-poke.gif","https://c.tenor.com/4OHxyGd4qp0AAAAC/boop-nose.gif","https://i.imgur.com/Zi4ahyj.gif", "https://i.imgur.com/Z4ZeNT1.gif", "https://c.tenor.com/y4R6rexNEJIAAAAC/boop-anime.gif"]
poke_names = ["Pokes you", "Touches You", "*uwu*", "Poking..."]

flick_gifs = ["https://c.tenor.com/PllSrSv3VF8AAAAC/flick-anime.gif","https://c.tenor.com/DGmwT7hYxoYAAAAM/ascendance-of-a-bookworm-head.gif","https://c.tenor.com/GdSggM7v5QkAAAAC/fairy-tail-flick.gif","https://c.tenor.com/-YundYgqXqEAAAAC/anime-aesthetic.gif","https://c.tenor.com/8V8pfc8yZfQAAAAd/toaru-index.gif","https://c.tenor.com/jRjDkuggsQIAAAAC/nagatoro-ijirinaide-nagatoro-san.gif","https://c.tenor.com/iYqV6Rqu7P8AAAAd/the-rising-of-tthe-shield-hero-anime.gif","https://c.tenor.com/ghknisaQrSoAAAAC/free-anime.gif"]
flick_names = ["Flicks you", "Finger bang you", "Flicks..."]

kiss_gifs = ["https://c.tenor.com/Yu2a1FmxFK8AAAAC/love-sweet.gif","https://c.tenor.com/7T1cuiOtJvQAAAAC/anime-kiss.gif","https://i.imgur.com/oXRW1XU.gif","https://gifimage.net/wp-content/uploads/2018/06/zero-no-tsukaima-louise-e-saito-gif-3.gif","https://i.imgur.com/sGVgr74.gif","https://www.icegif.com/wp-content/uploads/anime-kiss-icegif-1.gif","https://media0.giphy.com/media/QGc8RgRvMonFm/giphy.gif?cid=ecf05e47ia3gip25vpv7jyoo9g7rh1sm4xqig5tyd1vamqjc&rid=giphy.gif&ct=g","https://media1.giphy.com/media/zkppEMFvRX5FC/giphy.gif?cid=ecf05e47x8w8c4o0rt8m2j9u874ex85fk8vylhfx7yhwdes2&rid=giphy.gif&ct=g","https://media3.giphy.com/media/IdzovcoOUoUM0/giphy.gif?cid=ecf05e47x8w8c4o0rt8m2j9u874ex85fk8vylhfx7yhwdes2&rid=giphy.gif&ct=g","https://media2.giphy.com/media/G3va31oEEnIkM/giphy.gif?cid=ecf05e47x8w8c4o0rt8m2j9u874ex85fk8vylhfx7yhwdes2&rid=giphy.gif&ct=g"]
kiss_names = ["Kisses", "Kisses you", "*uwu*"]

hug_gifs = ["https://acegif.com/wp-content/gif/anime-hug-67.gif","https://i.pinimg.com/originals/ab/58/a8/ab58a8f3ad91fd62911f84bf3d54127c.gif","https://www.icegif.com/wp-content/uploads/elfin-lied-hugging.gif","https://data.whicdn.com/images/124011841/original.gif","https://i.imgur.com/nrdYNtL.gif","https://i.imgur.com/3OzmqMS.gif","https://media1.giphy.com/media/sUIZWMnfd4Mb6/giphy.gif","https://i.gifer.com/2QEa.gif","https://i.imgur.com/r9aU2xv.gif?noredirect","https://thumbs.gfycat.com/AlienatedUnawareArcherfish-size_restricted.gif"]
hug_names = ["*cuddles you*", "Hugs You", "Snuggles with you", "*snuggles you*"]

kick_gifs = ['https://c.tenor.com/LEgnGzli8VMAAAAC/anime-fight.gif','https://c.tenor.com/7te6q4wtcYoAAAAC/mad-angry.gif','https://c.tenor.com/2l13s2uQ6GkAAAAM/kick.gif','https://c.tenor.com/QxoBMmf2bRwAAAAC/jormungand-anime.gif','https://c.tenor.com/f1mFGp6vujkAAAAd/charlotte-window-kick-anime-kick.gif','https://c.tenor.com/kvxt9X-gXqQAAAAC/anime-clannad.gif','https://c.tenor.com/D67kRWw_cEEAAAAC/voz-dap-chym-dap-chym.gif','https://c.tenor.com/EcdG5oq7MHYAAAAM/shut-up-hit.gif','https://c.tenor.com/Lyqfq7_vJnsAAAAC/kick-funny.gif','https://c.tenor.com/4zwRLrLMGm8AAAAM/chifuyu-chifuyu-kick.gif']
kick_names = ['Boots You!', 'Kicks You!']

lick_gifs = ['https://i.imgur.com/bM6WrY9.gif','https://i.imgur.com/a7kNUdj.gif','https://i.imgur.com/H5DZMRQ.gif','https://i.imgur.com/SbzoXmp.gif','https://i.imgur.com/7uL0nIE.gif']
lick_names = ['Licks You...','Tounge Tickled']

class actionGifs(commands.Cog):
    
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command()
    async def punch(self, ctx: commands.Context,):
        embed = discord.Embed(
            colour=discord.Colour(0xCE3011),
            description=f"{ctx.author.mention} {(random.choice(punching_names))}"
            
        )
        embed.set_image(url=(random.choice(punching_gifs)))

        await ctx.send(embed = embed)

    @commands.command()
    async def poke(self, ctx: commands.Context):
        embed = discord.Embed(
            colour=(discord.Colour(0x832CE4)),
            description=f"{ctx.author.mention} {(random.choice(poke_names))}"
        )
        embed.set_image(url=(random.choice(poke_gifs)))

        await ctx.send(embed = embed)

    @commands.command()
    async def flick(self, ctx: commands.Context):
        embed = discord.Embed(
            colour=discord.Colour(0xE4882C),
            description=f"{ctx.author.mention} {(random.choice(flick_names))}"
        )
        embed.set_image(url=random.choice(flick_gifs))

        await ctx.send(embed = embed)

    @commands.command()
    async def kiss(self, ctx: commands.Context):
        embed = discord.Embed(
            colour=(discord.Colour(0xE42CC9)),
            description=f"{ctx.author.mention} {(random.choice(kiss_names))}"
        )
        embed.set_image(url=random.choice(kiss_gifs))

        await ctx.send(embed = embed)

    @commands.command(name='hug', aliases=['hugs', 'cuddle', 'cuddles'])
    async def hug(self,ctx: commands.Context):
        embed = discord.Embed(
            colour=(discord.Colour(0xE42C47)),
            description=f"{ctx.author.mention} {(random.choice(hug_names))}"
        )
        embed.set_image(url=random.choice(hug_gifs))

        await ctx.send(embed = embed)

    @commands.command(name='kick', aliases=['kicks'])
    async def kick(self,ctx: commands.Context):
        embed = discord.Embed(
            colour=(discord.Colour(0xE42C47)),
            description=f"{ctx.author.mention} {(random.choice(kick_names))}"
        )
        embed.set_image(url=random.choice(kick_gifs))

        await ctx.send(embed = embed)

    @commands.command(name='lick', aliases=['licks'])
    async def lick(self,ctx: commands.Context):
        embed = discord.Embed(
            colour=(discord.Colour(0xE42C47)),
            description=f"{ctx.author.mention} {(random.choice(lick_names))}"
        )
        embed.set_image(url=random.choice(lick_gifs))

        await ctx.send(embed = embed)