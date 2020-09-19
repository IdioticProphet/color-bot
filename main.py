import discord
import logging
from cogs.MiscCog import MiscCog
from cogs.ColorCog import ColorCog
from discord.ext import commands
from spacify import spacify


class DiscordBot(commands.Bot):
    # I make this a custom class in case we want to store global variables at some point
    def __init__(self, delims):
        super().__init__(delims)

if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)
    bot = DiscordBot("!")
    bot.add_cog(ColorCog(bot))
    bot.add_cog(MiscCog(bot))
    bot.run(open("/color-bot/token", "r").read())

