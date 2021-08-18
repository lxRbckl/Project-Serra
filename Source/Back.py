# Import <
from os import getcwd
from random import choice
from discord import Intents
from datetime import datetime as dt
from Serra import jsonLoad, jsonDump
from discord.ext.commands import Bot

# >


# Declaration
path = getcwd()[:-6]
setting = jsonLoad(f'{path}/Resources/Back')
Serra = Bot(command_prefix = '', intents = Intents.all())
token = ''

# >


@Serra.event
async def on_member_join(user):
    ''' user : class '''

    await user.send('Welcome to Serra.')
    jsonDump(f'{path}/Data/{str(user)}', [])


@Serra.command(aliases = ['Add', 'add'])
async def commandAdd(ctx, *args):
    ''' args[0] : str
        args[1] : int '''

    for key, value in setting['wordBank'].items():

        if (args[0] in value):

            data = jsonLoad(f'{path}/Data/{ctx.author}')
            data[0][key] += int(args[1])

            await ctx.author.send(f'{key} : {data[0][key]}', delete_after = 60)
            jsonDump(f'{path}/Data/{ctx.author}', data)


@Serra.command(aliases = ['weight', 'Weight'])
async def commandWeight(ctx, arg):
    ''' arg : float '''

    data = jsonLoad(f'{path}/Data/{ctx.author}')
    today = [{'Fiber' : 0,
              'Sugar' : 0,
              'Calorie' : 0,
              'Carbohydrate' : 0,
              'Weight' : float(arg),
              'Date' : f'{dt.now().day}-{dt.now().month}-{dt.now().year}'}]

    # Stack <
    [today.append(i) for i in data]

    # >

    jsonDump(f'{path}/Data/{ctx.author}', today)
    await commandGet(ctx)


@Serra.command(aliases = ['set', 'Set'])
async def commandSet(ctx, arg):
    ''' arg : str '''

    data = jsonLoad(f'{path}/Serra')
    data.append(arg)

    await ctx.author.send('Added.', delete_after = 60)
    jsonDump(f'{path}/Serra', data)


@Serra.command(aliases = ['get', 'Get'])
async def commandGet(ctx):
    '''  '''

    data = jsonLoad(f'{path}/Serra')

    await ctx.author.send(choice(data), delete_after = 1800) if (len(data) > 0) else (None)


# Run <
Serra.run(token)

# >
