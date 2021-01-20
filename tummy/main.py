import sys
import os


import tummy.notes
import tummy.weather
import tummy.reg


ARGC = len(sys.argv)
USAGE = """
    tummy [command] [arg1, arg2, arg3, etc...]
        For more help please use the 'help' command via `tummy help`
    """
HELP = """
    Commands:

    tummy weather
        Subcommands:
            
            1. config LATITUDE LONGITUDE UNITS

            Allowed units include: standard, imperial, metric.
            
            Example:
                tummy weather config 38.89511, -77.03637 standard
            

    tummy notes
        Subcommands:

            1. add NOTE

            Example:
                tummy notes add "Adding a note" works with and without quotes.

            Does exactly what the name suggests.

            2. remove NUMBER

            Example:
                tummy notes remove 1

            Does exactly what the name suggests.

            3. clear

            When you use this command you will be prompted to verify that you
            are actually sure you'd like to clear your notes.

            Example:
                tummy notes clear

            Does exactly what the name suggests.

            4. show

            This will be used by default if no subcommand is provided.

            Does exactly what the name suggests.

            Example:
                tummy notes
                tummy notes show


    tummy reg
        Subcommands:

            1. search LINK "REGULAR EXPRESSION"

            Example:
                tummy reg search https://theprogrammershangout.com/rules/ "\d\. [ -/:-~]+"

            Searches the provided link's text for all the matches of the
            regular expression that was provided


    tummy help
"""
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
    if command == "help":
        exit(tummy_help())
    elif command == "notes":
        n = tummy.notes.Notepad(NOTES_PATH)
        exit(tummy.notes.parse_note_args(subcommand, args, n))
    elif command == "reg":
        exit(tummy.reg.parse_reg_args(subcommand, args))
    elif command == "weather":
        w = tummy.weather.Weather(TUMMY_WEATHER)
        exit(tummy.weather.parse_weather_args(subcommand, args, w))
    else:
        print("\n    That's not a valid command.\n")
    

def main():
    os.chdir(f"/home/{os.getenv('USER')}")  
    parse_args(sys.argv)