import re


import requests
from bs4 import BeautifulSoup as bs


def make_request(link):
    rcount = 0
    while (r := requests.get(link)).status_code != 200:
        if rcount == 20:
            print(f"Tried {rcount} time to get a valid request, all failed.")
            return None
        print("Request failed, trying again.", r.status_code)
        rcount += 1
    return r


def search_request_text(response, expr, include_extra):
    expr = r"(.{,25}" + expr + r".{,25})" if include_extra else expr
    text = bs(response.text, "html.parser").stripped_strings
    regexpr = re.compile(expr)
    results = [result[0] for string in text if (result := regexpr.search(string)) != None]
    for n, result in enumerate(results, start=1):
        print(f"\n    Result {n}:\n\t{result}")
    print()


def parse_reg_args(subcommand, args):
    if subcommand == "search":
        if args:
            try:
                link = args[0]
                expr = args[1]
                include_extra = args[2] if len(args) == 3 else None
            except IndexError:
                print("\n    Please provide a regular exression to match with.\n")
            else:
                print(f"\n    Searching '{link}' with '{expr}'")
                response = make_request(link)
                if response:
                    search_request_text(response, expr, include_extra)
        else:
            print("\n    Please provide a link and a regular expression.\n")
    else:
        print("\n    Please provide a command.\n")