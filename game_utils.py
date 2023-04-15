import json
import pandas as pd

def get_Countries():
    with open('gameInfo/countries.json') as gamefile:
        countries=json.load(gamefile)
    return countries

def possible_Attacks(sit:dict,game:dict):
    cou_df : pd.DataFrame=sit["countries"]
    player=sit["turn"]
    ac=[]

    #get bordering countries with enough troups
    my_Areas=cou_df.loc[cou_df["owner"]==player]
    possibleAreas=my_Areas.loc[(my_Areas['border']==True) & (my_Areas['troups']>1)]


    #get the neighbouring countries
    for _,area in possibleAreas.iterrows():
        for nei in game['countries'][area['name']]:
            if nei not in my_Areas['name'].tolist():
                ac.append(area['name'],area)
    return ac