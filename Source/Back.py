# Import <
from random import choice
from discord import Intents
from os import getcwd, mkdir
from datetime import datetime as dt
from Serra import jsonLoad, jsonDump
from discord.ext.commands import Bot

# >


# Declaration
path = getcwd()[:-6]
setting = jsonLoad(f'{path}/Resources/Back')
serra = Bot(command_prefix = '', intents = Intents.all())
token = ''

# >


@serra.event
async def on_member_join(user):
    '''  '''

    await user.send('Welcome to Serra.')
    jsonDump(f'{path}/Data/{str(user)}', [])


@serra.command(aliases = ['Add', 'add'])
async def addFunction(ctx, *args):
    ''' args[0] : str
        args[1] : int '''

    for key, value in setting['wordBank'].items():

        if (args[0] in value):

            data = jsonLoad(f'{path}/Data/{ctx.author}')
            data[0][key] += int(args[1])

            await ctx.author.send(f'{key} : {data[0][key]}', delete_after = 60)
            jsonDump(f'{path}/Data/{ctx.author}', data)


@serra.command(aliases = ['weight', 'Weight'])
async def weightFunction(ctx, arg):
    ''' arg : float '''

    data = jsonLoad(f'{path}/Data/{ctx.author}')
    today = [{'Fiber' : 0,
              'Sugar' : 0,
              'Calories' : 0,
              'Carbohydrates' : 0,
              'Weight' : float(arg),
              'Date' : f'{dt.now().day}-{dt.now().month}-{dt.now().year}'}]

    # Stack <
    [today.append(i) for i in data]

    # >

    await getInspiration(ctx)
    jsonDump(f'{path}/Data/{ctx.author}', today)


@serra.command(aliases = ['status', 'Status'])
async def statusFunction(ctx, arg):
    '''  '''

    pass


@serra.command(aliases = ['set', 'Set'])
async def setInspiration(ctx, arg):
    ''' arg : str '''

    data = jsonLoad(f'{path}/Serra')
    data.append(arg)

    await ctx.author.send('Added.', delete_after = 60)
    jsonDump(f'{path}/Serra', data)


@serra.command(aliases = ['get', 'Get'])
async def getInspiration(ctx):
    '''  '''

    data = jsonLoad(f'{path}/Serra')

    await ctx.author.send(choice(data), delete_after = 1800) if (len(data) > 0) else (None)


# Run <
serra.run(token)

# >
