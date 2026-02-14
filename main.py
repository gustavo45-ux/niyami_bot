import discord
from discord.ext import commands
import os

intents = discord.Intents.all()
bot = commands.Bot(command_prefix="!", intents=intents)

async def load_cogs():
    for file in os.listdir("./bot/cogs"):
        if file.endswith(".py"):
            await bot.load_extension(f"bot.cogs.{file[:-3]}")

@bot.event
async def on_ready():
    print(f"Bot connecté : {bot.user}")
    await bot.tree.sync()

def run_bot():
    import asyncio
    asyncio.run(_start())

async def _start():
    await load_cogs()
    await bot.start(os.getenv("TOKEN") or "TON_TOKEN_BOT")
