from discord.ext import commands
from spacify import spacify
import requests


class MiscCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="echo", usage="!echo [message]", description="Echos what you say")
    async def echo(self, ctx, *, msg):
        await ctx.channel.send(msg)

    @commands.command(name="spacify", aliases=["spaceify", "verbose"] ,usage="!spacify [message]", description="does this -> D O E S T H I S")
    async def spacify(self, ctx, *, msg):
        await ctx.channel.send(spacify(msg))


    @commands.command(name="verse-of-the-day", aliases=["votd", "VOTD", "bible_me"], usage="!verse-of-the-day", description="its in the name")
    async def bible(self, ctx):
        resp = requests.get("https://beta.ourmanna.com/api/v1/get/?format=json")
        verse = f"\"{resp.json()['verse']['details']['text']}\" - {resp.json()['verse']['details']['reference']} {resp.json()['verse']['details']['version']}"
        await ctx.send(verse)
