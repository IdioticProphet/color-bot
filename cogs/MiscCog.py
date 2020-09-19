from discord.ext import commands
from spacify import spacify


class MiscCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="echo", usage="!echo [message]", description="Echos what you say")
    async def echo(self, ctx, *, msg):
        await ctx.channel.send(msg)

    @commands.command(name="spacify", aliases=["spaceify", "verbose"] ,usage="!spacify [message]", description="does this -> D O E S T H I S")
    async def spacify(self, ctx, *, msg):
        await ctx.channel.send(spacify(msg))


