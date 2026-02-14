import discord
from discord.ext import commands
import os

intents = discord.Intents.all()
bot = commands.Bot(command_prefix="!", intents=intents)

# -------- Cogs --------
async def load_cogs():
    for file in os.listdir("./bot/cogs"):
        if file.endswith(".py"):
            await bot.load_extension(f"bot.cogs.{file[:-3]}")

# -------- Events --------
@bot.event
async def on_ready():
    print(f"✅ Bot connecté : {bot.user}")
    await bot.tree.sync()

# -------- Lancement du bot --------
def run_bot():
    # On lance le bot avec asyncio et on charge les cogs
    import asyncio
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)

    async def start_bot():
        await load_cogs()
        await bot.start(os.getenv("BOT_TOKEN"))

    loop.run_until_complete(start_bot())
