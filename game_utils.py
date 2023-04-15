import json
import pandas as pd

def createGame(gamepath='gameInfo/testgame.json'):
    with open(gamepath) as gamefile:
        Game=json.load(gamefile)
    for cont in Game["continents"].keys():
        Game["continents"][cont]["members"]=set(Game["continents"][cont]["members"])
    return Game

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
                ac.append((area['name'],nei))
    return ac

def get_recruitment(sit:dict,game:dict):
    gain=game["basegain"]
    cou_df : pd.DataFrame=sit["countries"]
    player=sit["turn"]
    
    #area gain
    my_Areas=cou_df.loc[cou_df["owner"]==player]
    my_Areas=set(my_Areas["name"].tolist())
    gain+=game["tgain"][len(my_Areas)]

    #continent gain
    for cont in game["continents"].keys():
        if game["continents"][cont]["members"].issubset(my_Areas):
            gain+=game["continents"][cont]["gain"]

    return gain