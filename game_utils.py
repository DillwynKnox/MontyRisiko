import json
import pandas as pd

def get_Countries():
    with open('gameInfo/countries.json') as gamefile:
        countries=json.load(gamefile)
    return countries

def possible_Attacks():
    pass