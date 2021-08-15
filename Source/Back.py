# Import <
from os import getcwd
from discord import Intents
from datetime import datetime as dt
from Serra import jsonLoad, jsonDump
from discord.ext.commands import Bot

# >


# Declaration
path = getcwd()[:-6]
setting = jsonLoad(f'{path}/Resources/Back')
serra = Bot(command_prefix = '', intents = Intents.all())
token = 'ODY4MDE2OTIyNjM2MjAyMDM2.YPphwQ.1ajuE09cOuICGvF9_P_WPCS_afg'

# >


@serra.command(aliases = ['Add', 'add'])
async def addFunction(ctx, *args):
    ''' args[0] : str
        args[1] : int '''

    for key, value in setting['wordBank'].items():

        # If Valid <
        if (args[0] in value):

            data = jsonLoad(f'{path}/Data/{ctx.author}')
            data[0][key] + int(args[1])

            await ctx.author.send(f'{key} : {data[0][key]}', delete_after = 60)
            await jsonDump(f'{path}/Data/{ctx.author}', data)

        # >


@serra.command(aliases = ['weight', 'Weight'])
async def weightFunction(ctx, arg):
    ''' arg : float '''

    # Declaration <
    data = jsonLoad(f'{path}/Data/{ctx.author}')
    today = [{'Fiber' : 0,
              'Sugar' : 0,
              'Calories' : 0,
              'Carbohydrates' : 0,
              'Weight' : float(arg),
              'Date' : f'{dt.now().day}-{dt.now().month}-{dt.now().year}'}]

    # >

    # Stack <
    [today.append(i) for i in data]

    # >

# Run <


# >
