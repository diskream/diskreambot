# -*- coding: utf-8 -*
import random

import discord
from random import randint, choice
from discord.ext import commands, tasks
from config import *
import re
import numpy as np
from settings import settings

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
    if re.findall(r'[?]', message.content) and message.author == client.get_user(unique_users['checka']):
        await message.reply('Заебал ныть')
    if message.author == client.get_user(unique_users['suvik']) and random.choice(np.arange(0, 100)) <= 70:
        await message.reply('Я этой крысе носатой ничего делать не буду!')
    elif message.author == client.get_user(unique_users['checka']) and random.choice(np.arange(0, 100)) <= 70:
        await message.reply('Я с Артемами не разговариваю')
    elif random.choice(np.arange(0, 100)) <= 7:
        await message.reply('Именно ТЫ получаешь возможность быть посланным нахуй! До связи.')
        await message.reply('CheckaBot покинул чат.')
        return
    if re.findall(r'([Уу][Кк][Рр][АаОо][Ии][Нн])|([Uu][Kk][Rr][Aa][Ii][Nn][Ee])', message.content):
        await message.reply('Героям слава!')
    elif re.findall(r'([Чч][Ее][Кк][Аа])|([Чч][Кк][Чч])', message.content):
        await message.reply('Этого типа же Артемом зовут?\nГосподи, как можно было человека назвать АРТЕМОМ???')
    for word in message.content.lower().split():
        if word in bad_words:
            await message.reply('Без негатива.')
        if re.findall(r'([Аа][Рр][Тт][ЕеЁё][Мм])| ([Тт][ЕеЁё][Мм][Аа])'):
            await message.reply('Господи, как можно было человека назвать ЭТИМ именем???')


@client.command()
async def add(comm, left, right):
    try:
        await comm.send(int(left) + int(right))
    except Exception:
        await comm.send(str(left) + ' ' + str(right))



@client.command()
async def help_me(comm):
    await comm.send(help_description)



@client.command()
async def roll(ctx, end, start=0):
    try:
        await ctx.send(randint(int(start), int(end)))
    except:
        to_send = f'{ctx.author.mention}, 4ел, как я тебе буду рандомить' + ' ' + end + '?'
        await ctx.send(to_send)




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
async def compliment(ctx, member: discord.Member = 0):
    if member == 0:
        member = ctx.author
        await ctx.send('{0.mention},{1}'.format(member, choice(compliments)))
    else:
        await ctx.send('{0.mention},{1}'.format(member, choice(compliments)))



# connecting bot to the server via token
client.run(settings['token'])
