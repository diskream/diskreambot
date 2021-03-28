# -*- coding: utf-8 -*

import discord
from random import randint, choice
from discord.ext import commands, tasks
from config import settings, help_description, insult_list, ukraine, jokes, bad_words, compliments
import re

intents = discord.Intents.default()
intents.members = True
client = commands.Bot(command_prefix='!!', intents=intents)
author = client.get_user(int())
@client.event
async def on_ready():
    game_status.start()
    print('Подключился к серверу как:', client.user.name, client.user.id)


@tasks.loop()
async def game_status():
    await client.change_presence(activity=discord.Game('в очке пальчиком'))


@client.listen('on_message')
async def on_message(message):
    question = re.findall(r'\D?', message.content)
    if '?' in question and message.author == client.get_user(452404350124294154):
        await message.channel.send('Заебал ныть')
    if message.author == client.get_user(374292501814706176) and randint(0, 10) == 7:
        await message.channel.send('Я этой крысе носатой ничего делать не буду!')
    elif message.author == client.get_user(452404350124294154) and randint(0, 10) == 7:
        await message.channel.send('Я с Артемами не разговариваю')
    elif randint(0, 30) == 7:
        await message.channel.send('Именно ТЫ получаешь возможность быть посланным нахуй! До связи.')
        await message.channel.send('CheckaBot покинул чат.')
        return
    if message.content.startswith(ukraine):
        await message.channel.send('Героям слава!')
    elif message.content.startswith(('чека', 'Чека', 'Чекаче', 'чкч', 'Чекалин')):
        await message.channel.send('Этого типа же Артемом зовут?')
        await message.channel.send('Господи, как можно было человека назвать АРТЕМОМ???')
    for word in message.content.lower().split():
        if word in bad_words:
            await message.channel.send('Без негатива.')
        if word in ('артём', 'артем', 'тема', 'тёма', 'темочка', 'тёмочка'):
            await message.channel.send('Господи, как можно было человека назвать ЭТИМ именем???')


@client.command()
async def add(comm, left, right):
    try:
        await comm.send(int(left) + int(right))
    except:
        await comm.send(str(left) + ' ' + str(right))


@client.command()
async def сложить(comm, left, right):
    await add(comm, left, right)


@client.command()
async def help_me(comm):
    await comm.send(help_description)


@client.command()
async def помощь(comm):
    await help_me(comm)


@client.command()
async def roll(ctx, end, start=0):
    try:
        await ctx.send(randint(int(start), int(end)))
    except:
        to_send = f'{ctx.author.mention}, 4ел, как я тебе буду рандомить' + ' ' + end + '?'
        await ctx.send(to_send)


@client.command()
async def ролл(ctx, end, start=0):
    await roll(ctx, end, start)


@client.command()
async def hui(ctx, member: discord.Member = 0):
    if member == 0:
        await ctx.send(f'{ctx.author.mention},' + ' ты к кому обращаешься-то?')
    await ctx.send('{0.mention}, {1}'.format(member, choice(insult_list)))


@client.command()
async def хуй(ctx, member: discord.Member = 0):
    await hui(ctx, member)


@client.command()
async def joke(ctx):
    await ctx.send(choice(jokes))


@client.command()
async def шутка(ctx):
    await joke(ctx)


@client.command()
async def Шутка(ctx):
    await joke(ctx)


@client.command()
async def compliment(ctx, member: discord.Member = 0):
    if member == 0:
        member = ctx.author
        await ctx.send('{0.mention},{1}'.format(member, choice(compliments)))
    else:
        await ctx.send('{0.mention},{1}'.format(member, choice(compliments)))


@client.command()
async def комплимент(ctx, member: discord.Member = 0):
    await compliment(ctx, member)


# connecting bot to the server via token
client.run(settings['token'])
