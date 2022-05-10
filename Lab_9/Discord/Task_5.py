import discord
from tokens import D_TOKEN

client = discord.Client()


@client.event
async def on_ready():
    print(f'{client.user} подключен к Discord!')
    for guild in client.guilds:
        print(
            f'{client.user} подключились к чату и готов показать котика (или пёсика!):\n'
            f'{guild.name}(id: {guild.id})'
        )


@client.event
async def on_message(ctx):
    if ctx.author != client.user:
        if 'кот' in str.lower(ctx.content):
            await ctx.channel.send(file=discord.File('kiten.jpg'))
        elif 'собака' in str.lower(ctx.content):
            await ctx.channel.send(file=discord.File('dog.jpg'))


client.run(D_TOKEN)
