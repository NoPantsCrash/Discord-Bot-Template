
from discord.ext import commands


class Dummy(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(aliases=['dummy','help'])
    async def test(self, ctx):
        author = ctx.message.author.id
        await ctx.send(f"{ctx.author.mention}  This is a demo cog :)")


def setup(client):
    client.add_cog(Dummy(client))
