import json
import pandas as pd
import random

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
    cou_df : pd.DataFrame=sit["countries"]
    player=sit["turn"]
    
    #base gain
    gain=game["basegain"]
    
    #area gain
    my_Areas=cou_df.loc[cou_df["owner"]==player]
    my_Areas=set(my_Areas["name"].tolist())
    gain+=game["tgain"][len(my_Areas)]

    #continent gain
    for cont in game["continents"].keys():
        if game["continents"][cont]["members"].issubset(my_Areas):
            gain+=game["continents"][cont]["gain"]
    
    #TODO CARDS????

    return gain

#initialzize the game
def initialize(game:dict):
    countrylist=list(game["countries"].keys())
    playercount=len(game["players"].keys())
    initial_situation={}

    

    countrydfbase=[]
    #assign countries
    random.shuffle(countrylist)
    for pn in range(playercount):
        mycountries=countrylist[playercount-pn-1::playercount]
        mycc=len(mycountries)
        remaintroups=game["startTroops"]-mycc
        #determine troups
        troups=[random.randint(1,1000) for _ in mycountries]
        troups=list(map(lambda x: int(x/sum(troups) * remaintroups)+1,troups))
        if sum(troups)!= game["startTroops"]:
            miss=sum(troups)-game["startTroops"]
            i=random.randint(0,mycc-1)
            troups[i]=troups[i]-miss
        
        #determine if border
        border=[True]*mycc
        for i in range(mycc):
            if set(game["countries"][mycountries[i]]).issubset(mycountries):
                border[i]=False
        

        myc=list(zip(mycountries,[pn]*mycc,border,troups))
        countrydfbase+=myc

    initial_situation["countries"]=pd.DataFrame(countrydfbase,columns=["name","owner","border","troups"])
    initial_situation["turn"]=0

    return initial_situation
    
        
        

