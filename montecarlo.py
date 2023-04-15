from abc import ABC,abstractmethod
from math import sqrt,log,inf

class Node(ABC):

    @abstractmethod
    def make_children(self):
        pass

    @abstractmethod
    def get_random_child(self):
        pass

    @abstractmethod
    def get_player(self):
        pass

    @abstractmethod
    def is_terminal(self) -> bool:
        pass
    
    @abstractmethod
    def get_score(self):
        pass


class Montycarlo():
    N=0
    def __init__(self,numberofPlayers,gameNode:Node) -> None:
        self.myNode=gameNode
        self.nplayers=numberofPlayers
        self.n=0
        self.v=[0]*numberofPlayers
        self.childs=[]
        self.player=gameNode.get_player()

    def rollout(self):
        anode=self.myNode
        while not anode.is_terminal():
            anode=anode.get_random_child()
        return anode.get_score()
    
    def makechilds(self):
        allfollowNodes=self.myNode.make_children()
        for node in allfollowNodes:
            self.childs.append(Montycarlo(self.nplayers,self,node))
    
    @staticmethod
    def ucb(self,n,v):
        if n==0:
            return inf
        return v/n+2*sqrt(log(Montycarlo.N)/n)
    
    def score_ucb(self,node):
        return Montycarlo.ucb(node.n,node.v[self.player])


    def getBestchild(self):
        return max(self.childs,key=self.score_ucb)

    def addv(self,newv):
        self.v=list(map(lambda x,y:x+y,self.v,newv))

    def simulate(self):
        self.n+=1
        if not self.childs:
            if self.n==1:
                newv=self.rollout()
            else:
                if self.makechilds():
                    newv=self.childs[0].simulate()           
        else:
            bestc=self.getBestchild()
            newv=bestc.simulate()
        
        self.addv(newv)
        return newv
        

    
