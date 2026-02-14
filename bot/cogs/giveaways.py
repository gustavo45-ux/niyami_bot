from discord.ext import commands

class Giveaway(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def start_giveaway(self, ctx, prize: str):
        await ctx.send(f"🎉 Giveaway commencé pour : {prize} !")

async def setup(bot):
    await bot.add_cog(Giveaway(bot))
