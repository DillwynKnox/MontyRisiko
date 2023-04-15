import unittest
import pandas as pd
from game_utils import possible_Attacks,createGame,get_recruitment





class TestGameUtils(unittest.TestCase):
    def __init__(self, methodName: str = "runTest") -> None:
        super().__init__(methodName)
        self.exampleGame=createGame()
        troups=[1]*8
        troups[1]=4
        exampleCountries=pd.DataFrame(
            {"name": self.exampleGame["countries"].keys(),
            "owner": [0,0,1,0,0,2,1,2],
            "border":[False,True,True,True,True,True,True,True],
            "troups":troups},
            index=[0,1,2,3,4,5,6,7])
        self.exampleSit={
            "countries":exampleCountries,
            "turn":0
        }

    def test_createGame(self):
        testgame=createGame()
        self.assertEqual(len(testgame["countries"].keys()),8)
        self.assertEqual(len(testgame["players"].keys()),3)

    def test_possibleAttacks(self):
        self.assertEqual(possible_Attacks(self.exampleSit,self.exampleGame),[("NRW","Preussen")])

    def test_recruit(self):
        self.assertEqual(get_recruitment(self.exampleSit,self.exampleGame),7)


if __name__== '__main__':
    unittest.main()
