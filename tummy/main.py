import sys
import os


import tummy.notes
import tummy.weather


ARGC = len(sys.argv)
USAGE = """
    tummy [command] [arg1, arg2, arg3, etc...]
        For more help please use the 'help' command via `tummy help`
    """
HELP = """
    commands:

        weather OPTIONAL:[ config [LAT LON UNITS] ]
            Allowed units include: standard, imperial, metric.
            By default the arguments will be given these values resectively:
                38.89511, -77.03637 "standard"
            Learn more: https://openweathermap.org/api/one-call-api#data

        notes [ add, remove, clear, show ]
"""
MULTI_ARG_COMMANDS = ['notes']
NOTES_PATH = ".tummy_notes.json"
TUMMY_WEATHER = ".tummy_weather.json"


def tummy_help():
    print(HELP)


def parse_args(args):
    # Deal with the amount of arguments given
    if ARGC == 1:
        print(USAGE)
        return
    elif ARGC == 2:
        command = sys.argv[1].lower()
        subcommand = None
        args = None
    elif ARGC >= 3:
        command = sys.argv[1].lower()
        subcommand = sys.argv[2].lower()
        args = arguments if len((arguments := sys.argv[3:])) != 0 else None
    

    # Deal with the commands.
    if command == "weather":
        w = tummy.weather.Weather(TUMMY_WEATHER)
        exit(tummy.weather.parse_weather_args(subcommand, args, w))
    elif command == "help":
        exit(tummy_help())
    elif command == "notes":
        n = tummy.notes.Notepad(NOTES_PATH)
        exit(tummy.notes.parse_note_args(subcommand, args, n))
    else:
        print("\n    That's not a valid command.\n")
    

def main():
    os.chdir(f"/home/{os.getenv('USER')}")  
    parse_args(sys.argv)