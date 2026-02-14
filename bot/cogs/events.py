import discord
from discord.ext import commands

class Events(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.tree.command(name="event")
    async def event(self, interaction: discord.Interaction, titre: str, date: str):
        embed = discord.Embed(title=f"📅 {titre}", description=f"Date: {date}\nRéagis avec ✅ pour participer", color=0x2ecc71)
        msg = await interaction.channel.send(embed=embed)
        await msg.add_reaction("✅")
        await interaction.response.send_message("Event créé !", ephemeral=True)

async def setup(bot):
    await bot.add_cog(Events(bot))
