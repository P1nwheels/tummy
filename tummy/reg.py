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


def search_request_text(link, expr, include_extra):
    response = make_request(link)
    if not response:
        return None
    expr = r"(.{,50}" + expr + r".{,50})" if include_extra == "yes" else r"(" + expr + r")"
    text = bs(response.text, "lxml").stripped_strings
    regexpr = re.compile(expr)
    results = [result.groups() for string in text if (result := regexpr.search(string)) != None]
    for n, result in enumerate(results, start=1):
        print(f"\nResult {n}:\n    {result}")
    print()


def parse_reg_args(subcommand, subcommand_args):
    if subcommand == "search":
        if len(subcommand_args) == 3:
            if subcommand_args[2] in {"yes", "no"}:
                search_request_text(*subcommand_args)
            else:
                print("\nINCLUDE_EXTRA may be only one of the two: [yes] [no]\n")
        else:
            print("\nPlease provide the proper number of arguments\n")
    else:
        print("\nPlease provide a command.\n")