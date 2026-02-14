import discord
from discord.ext import commands

class TicketView(discord.ui.View):
    @discord.ui.button(label="Créer un ticket", style=discord.ButtonStyle.green)
    async def create_ticket(self, interaction: discord.Interaction, button: discord.ui.Button):
        overwrites = {
            interaction.guild.default_role: discord.PermissionOverwrite(read_messages=False),
            interaction.user: discord.PermissionOverwrite(read_messages=True)
        }

        channel = await interaction.guild.create_text_channel(f"ticket-{interaction.user.name}", overwrites=overwrites)
        await interaction.response.send_message(f"Ticket créé : {channel.mention}", ephemeral=True)

class Tickets(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.tree.command(name="ticket_panel")
    async def ticket_panel(self, interaction: discord.Interaction):
        await interaction.response.send_message("Clique pour créer un ticket :", view=TicketView())

async def setup(bot):
    await bot.add_cog(Tickets(bot))
