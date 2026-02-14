import discord
from discord.ext import commands
import random

class Giveaways(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.tree.command(name="giveaway")
    async def giveaway(self, interaction: discord.Interaction, prize: str):
        embed = discord.Embed(title="🎉 Giveaway", description=f"Réagis avec 🎉 pour gagner\nPrix : {prize}", color=0x5865F2)
        msg = await interaction.channel.send(embed=embed)
        await msg.add_reaction("🎉")
        await interaction.response.send_message("Giveaway lancé !", ephemeral=True)

async def setup(bot):
    await bot.add_cog(Giveaways(bot))
