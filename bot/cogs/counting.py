from discord.ext import commands

class Counting(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def count(self, ctx, number: int):
        await ctx.send(f"Le prochain nombre est : {number + 1}")

async def setup(bot):
    await bot.add_cog(Counting(bot))
