import unittest
import pandas as pd
from game_utils import possible_Attacks,createGame





class TestGameUtils(unittest.TestCase):
    def test_createGame(self):
        testgame=createGame()
        self.assertEqual(len(testgame["countries"].keys()),8)

    def test_possibleAttacks(self):
        exampleGame=createGame()
        troups=[1]*8
        troups[1]=4
        exampleCountries=pd.DataFrame(
            {"name": exampleGame["countries"].keys(),
            "owner": [0,0,1,0,0,2,1,2],
            "border":[False,True,True,True,True,True,True,True],
            "troups":troups},
            index=[0,1,2,3,4,5,6,7])
        exampleSit={
            "countries":exampleCountries,
            "turn":0
        }
        self.assertEqual(possible_Attacks(exampleSit,exampleGame),[("NRW","Preussen")])




if __name__== '__main__':
    unittest.main()
