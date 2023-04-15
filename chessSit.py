from math import sqrt, log, inf
import random
from montecarlo import Node,Montycarlo
import chess

class ChessNode(Node):
    def __init__(self, board:chess.Board, player,level=0):
        self.board = board
        self.player = player
        self.level=level

    def make_children(self):
        children = []
        moves = self.board.legal_moves
        for move in moves:
            child_board = self.board.copy()  # Create a copy of the board for the child node
            child_board.push(move)
            child_player = (self.player+1) % 2
            child_node = ChessNode(child_board, child_player,self.level+1)
            children.append(child_node)
        return children

    def get_random_child(self):
        child_board = self.board.copy()
        moves = list(child_board.legal_moves)
        move = random.choice(moves)
        
        child_board.push(move)
        child_player = self.board.child_player = (self.player+1) % 2
        return ChessNode(child_board, child_player,self.level+1)

    def get_player(self):
        return self.player

    def is_terminal(self):
        if self.level>=1000:
            return True
        return self.board.is_game_over()

    def get_score(self):
        if self.level>=1000:
            return [0.5,0.5]
        scores = [0.5, 0.5]  # Assuming draw by default
        if self.board.is_checkmate():
            scores[self.get_winner()] = 1.0
            scores[self.get_loser()] = 0.0
        elif self.board.is_stalemate() or self.board.is_insufficient_material() \
                or self.board.is_seventyfive_moves() or self.board.is_fivefold_repetition() \
                or self.board.is_fifty_moves():
            pass  # Draw, scores remain [0.5, 0.5]
        return scores
    
    def get_winner(self):
        result = self.board.result()
        if result == '1-0':
            return 0
        elif result == '0-1':
            return 1
        else:
            return None

    def get_loser(self):
        winner = self.get_winner()
        if winner is not None:
            return 1 - winner
        else:
            return None


def getBoard(Board):
    sit=ChessNode(Board,0)
    monty=Montycarlo(2,sit)
    for _ in range(100):
        monty.simulate()
    return monty.getEndChild().myNode.board

if __name__=="__main__":
    print(getBoard(chess.Board()))