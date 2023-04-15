from montecarlo import Node,Montycarlo
import random
class TicToeSit(Node):
    def __init__(self,player,nplay,board) -> None:
        self.player=player
        self.nplayer=nplay
        self.board=board
    
    def make_children(self):
        indices = [i for i, x in enumerate(self.board) if x == "_"]
        childs=[]
        for i in indices:
            newboard=self.board.copy()
            newboard[i]=self.player
            childs.append(TicToeSit((self.player+1)%2,
                                    2,
                                    newboard))
        return childs

    def get_random_child(self):
        indices = [i for i, x in enumerate(self.board) if x == "_"]
        newboard=self.board.copy()
        change=random.choice(indices)
        newboard[change]=self.player
        return TicToeSit((self.player+1)%2,2,newboard)
    
    def get_player(self) -> int:
        return self.player
    
    def is_terminal(self) -> bool:
        winning_combinations = [(0, 1, 2), (3, 4, 5), (6, 7, 8),  # Rows
                                (0, 3, 6), (1, 4, 7), (2, 5, 8),  # Columns
                                (0, 4, 8), (2, 4, 6)]             # Diagonals

        for comb in winning_combinations:
            if self.board[comb[0]] == self.board[comb[1]] == self.board[comb[2]] and self.board[comb[0]] != "_":
                if self.board[comb[0]] == 0:
                    return True
                else:
                    return True

        if "_" not in self.board:
            return True
        else:
            return False
        
    def get_score(self) -> list:
        winning_combinations = [(0, 1, 2), (3, 4, 5), (6, 7, 8),  # Rows
                                (0, 3, 6), (1, 4, 7), (2, 5, 8),  # Columns
                                (0, 4, 8), (2, 4, 6)]             # Diagonals

        for comb in winning_combinations:
            if self.board[comb[0]] == self.board[comb[1]] == self.board[comb[2]] and self.board[comb[0]] != "_":
                if self.board[comb[0]] == 0:
                    return [1, 0]
                else:
                    return [0, 1]

        if "_" not in self.board:
            return [0.2, 0.2]
        else:
            return None

myboard=["_"]*9
myboard=[0,'_',1,'_','_','_','_','_','_']
position=TicToeSit(0,2,myboard)
myMont=Montycarlo(2,position)

for _ in range(10000):
    myMont.simulate()
print(myMont.getEndChild().myNode.board)