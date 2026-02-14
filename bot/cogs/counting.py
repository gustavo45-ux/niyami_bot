import discord
from discord.ext import commands
from database import connect

class Counting(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author.bot or not message.guild:
            return

        conn = connect()
        c = conn.cursor()
        c.execute("SELECT counting_enabled FROM guild_config WHERE guild_id=?", (message.guild.id,))
        row = c.fetchone()

        if row and row[0] == 1:
            try:
                int(message.content)
                await message.add_reaction("✅")
            except:
                pass

        conn.close()
        await self.bot.process_commands(message)

async def setup(bot):
    await bot.add_cog(Counting(bot))
