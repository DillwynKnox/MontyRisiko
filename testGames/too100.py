from montecarlo import Node, Montycarlo
from random import randint

class Situation100(Node):
    def __init__(self,player,number,numberofPlayers) -> None:
        super().__init__()
        self.number=number
        self.player=player
        self.nplayer=numberofPlayers
    
    def make_children(self):
        childs=[Situation100((self.player+1)%self.nplayer,
                             self.number+i,
                             self.nplayer)
                            for i in range(1,11)]
        return childs
    
    def get_player(self):
        return self.player
    
    def is_terminal(self) -> bool:
        return self.number>=90
    
    def get_score(self):
        scores=[0]*self.nplayer
        scores[self.player]=1
        return scores
    def get_random_child(self):
        return Situation100((self.player+1)%self.nplayer,
                             self.number+randint(1,10),
                             self.nplayer)

if __name__=="__main__":
    PLAYERNUM=2
    while True:
        currentNumb=input()
        currentNumb=int(currentNumb)
        start=Situation100(0,currentNumb,PLAYERNUM)
        mysolver=Montycarlo(PLAYERNUM,start)
        for _ in range(100000):
            mysolver.simulate()
        print(f'Say {mysolver.getBestchild().myNode.number}!!!')


