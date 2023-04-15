from math import sqrt, log, inf
import random
from montecarlo import Node,Montycarlo
from chessboard import Board
import chess

class ChessNode(Node):
    def __init__(self, board, player,level=0):
        self.board = Board(board)
        self.player = player
        self.level=level

    def make_children(self):
        children = []
        moves = self.board.get_all_moves(self.player)
        for move in moves:
            child_board = self.board.copy()  # Create a copy of the board for the child node
            child_board.make_move(move)
            child_player = self.board.get_next_player(self.player)
            child_node = ChessNode(child_board, child_player,self.level+1)
            children.append(child_node)
        return children

    def get_random_child(self):
        child_board = self.board.copy()
        moves = child_board.get_all_moves(self.player)
        move = random.choice(moves)
        
        child_board.make_move(move)
        child_player = self.board.get_next_player(self.player)
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
        scores = self.board.get_scores()
        return scores

def getBoard(Board):
    sit=ChessNode(Board,0)
    monty=Montycarlo(2,sit)
    for _ in range(1000):
        monty.simulate()
    return monty.getEndChild.myNode.board

if __name__=="__main__":
    print(getBoard(chess.Board()))