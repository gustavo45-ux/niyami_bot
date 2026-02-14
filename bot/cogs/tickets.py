from discord.ext import commands

class Tickets(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def ticket(self, ctx, *, reason: str):
        await ctx.send(f"🎫 Ticket créé pour : {reason}")

async def setup(bot):
    await bot.add_cog(Tickets(bot))
