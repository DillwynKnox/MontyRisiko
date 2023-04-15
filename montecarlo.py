from abc import ABC,abstractmethod
from math import sqrt,log,inf

class Node(ABC):

    @abstractmethod
    def make_children(self) -> list:
        pass

    @abstractmethod
    def get_random_child(self):
        pass

    @abstractmethod
    def get_player(self) -> int:
        pass

    @abstractmethod
    def is_terminal(self) -> bool:
        pass
    
    @abstractmethod
    def get_score(self) -> list:
        pass


class Montycarlo():
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
        if self.myNode.is_terminal():
            return False
        allfollowNodes=self.myNode.make_children()
        for node in allfollowNodes:
            self.childs.append(Montycarlo(self.nplayers,node))
        return True
    
    @staticmethod
    def ucb(n,v,logN):
        if n==0:
            return inf
        return v/n+2*sqrt(logN/n)
    
    def score_ucb(self,node):
        logN=log(self.n)
        return Montycarlo.ucb(node.n,node.v[self.player],logN)


    def getBestchild(self):
        return max(self.childs,key=self.score_ucb)

    def addv(self,newv):
        self.v=list(map(lambda x,y:x+y,self.v,newv))
    
    def score(self,node):
        return node.v[self.player]/node.n
    
    def getEndChild(self):
        return max(self.childs,key=self.score)

    def simulate(self):
        self.n+=1
        if not self.childs:
            if self.n==1:
                newv=self.rollout()
            else:
                if self.makechilds():
                    newv=self.childs[0].simulate()
                else:
                    newv=self.rollout()        
        else:
            bestc=self.getBestchild()
            newv=bestc.simulate()
        
        self.addv(newv)
        return newv
        

    
