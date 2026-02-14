import discord
from discord.ext import commands
import os
import asyncio

intents = discord.Intents.all()
bot = commands.Bot(command_prefix="!", intents=intents)

# -------- Charger les cogs --------
async def load_cogs():
    for file in os.listdir("./bot/cogs"):
        if file.endswith(".py"):
            await bot.load_extension(f"bot.cogs.{file[:-3]}")

# -------- Events --------
@bot.event
async def on_ready():
    print(f"✅ Bot connecté : {bot.user}")
    await bot.tree.sync()

# -------- Fonction pour lancer le bot --------
def run_bot():
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)

    async def start_bot():
        await load_cogs()
        await bot.start(os.getenv("BOT_TOKEN"))

    loop.run_until_complete(start_bot())
