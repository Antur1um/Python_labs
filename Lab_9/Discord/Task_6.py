import discord
from discord.ext import commands
from time import sleep
from tokens import D_TOKEN


class BotTimer(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(name='timer')
    async def timer(self, ctx, seconds):
        sleep(int(seconds))
        await ctx.send("время X наступило!")


client = commands.Bot(command_prefix='/')
client.add_cog(BotTimer(client))
client.run(D_TOKEN)
