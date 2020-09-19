import discord
import logging
from discord.ext import commands
from spacify import spacify

def is_valid_hex(candidate):
    try:
        assert candidate.startswith("#")
        hex(int(candidate[1:], 16))
    except ValueError:
        return False

    except AssertionError:
        return False

    return True

class MiscCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="echo", usage="!echo [message]", description="Echos what you say")
    async def echo(self, ctx, *, msg):
        await ctx.channel.send(msg)

    @commands.command(name="spacify", aliases=["spaceify", "verbose"] ,usage="!spacify [message]", description="does this -> D O E S T H I S")
    async def spacify(self, ctx, *, msg):
        await ctx.channel.send(spacify(msg))


class ColorCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.group(name="color", aliases=["c"], usage="!color #[color code]", description="Gives your name a color")
    async def role(self, ctx):
        if ctx.invoked_subcommand is None:
            await ctx.channel.send("""
```
Color Command:
    - add #[colorcode] : given colorcode is valid, add color to your role
    - remove          : remove your colorcode
```
""")

    @role.group(name="add")
    async def add_role(self, ctx, hexcolor):
        for role in ctx.author.roles:
            if role.name[0] == "#" and is_valid_hex(role.name[1:]):
                await ctx.channel.send("You already have a color!")
                return
        if not is_valid_hex(hexcolor):
            if hexcolor.startswith("#"):
                await ctx.channel.send("You didnt supply a valid number")
            else:
                await ctx.channel.send("Didn't start with a #")
            return
        color_code = int(hexcolor[1:].upper(), 16)
        default_role = ctx.guild.default_role
        role = await ctx.guild.create_role(name=hexcolor, color=discord.Color(color_code))
        await ctx.message.author.add_roles(role)
        await ctx.channel.send(f"Added {hexcolor} to {ctx.message.author}")

    @role.group(name="remove")
    async def remove_role(self, ctx):
        roles = ctx.message.author.roles
        for role in roles:
            if is_valid_hex(role.name):
                await ctx.author.remove_roles(role)
                await ctx.channel.send(f"removed role {role} from {ctx.message.author}")
                return

if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)
    TOKEN = "NzQ1Njc3MDQwNDEzNDQyMTE4.Xz1P3A.MYvDqIjKdkvf7aixSNwSMnNzx6Y"
    bot = commands.Bot("!")
    bot.add_cog(ColorCog(bot))
    bot.add_cog(MiscCog(bot))
    bot.run(TOKEN)

