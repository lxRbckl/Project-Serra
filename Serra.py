# Project Serra by Highlander #


# Import <
from json import load, dump

# >


def jsonLoad(arg):
    ''' arg : str '''

    with open(f'{arg}.json', 'r') as fileVariable:

        return load(fileVariable)


def jsonDump(*args):
    ''' args[0] : str
        args[1] : dict '''

    with open(f'{args[0]}.json', 'w') as fileVariable:

        dump(args[1], fileVariable, indent = 4)
