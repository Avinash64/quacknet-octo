import os
import logging

import discord
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.environ["DISCORD_TOKEN"]

log = logging.getLogger(__name__)

# Prefix commands read message text, so message_content is REQUIRED here
# AND must be toggled on in the Developer Portal.
intents = discord.Intents.default()
intents.message_content = True


class QuacknetBot(commands.Bot):
    def __init__(self):
        super().__init__(command_prefix=",", intents=intents)

    async def on_ready(self):
        log.info("Logged in as %s (id: %s)", self.user, self.user.id)


bot = QuacknetBot()


@bot.command(name="ping")
async def ping(ctx: commands.Context):
    await ctx.send("Pong!")


if __name__ == "__main__":
    bot.run(TOKEN)