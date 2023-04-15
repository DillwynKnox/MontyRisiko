import chess

class Board:
    def __init__(self,board:chess.Board):
        self.board = board

    def get_all_moves(self, player):
        moves = []
        for move in self.board.board.legal_moves:
            if self.is_valid_move(move, player):
                moves.append(move)
        return moves

    def make_move(self, move):
        self.board.push(move)

    def get_next_player(self, player):
        return (player+1)%2

    def is_game_over(self):
        return self.board.is_game_over()
        
    def get_scores(self):
        scores = [0.5, 0.5]  # Assuming draw by default
        if self.board.is_checkmate():
            scores[self.get_winner()] = 1.0
            scores[self.get_loser()] = 0.0
        elif self.board.is_stalemate() or self.board.is_insufficient_material() \
                or self.board.is_seventyfive_moves() or self.board.is_fivefold_repetition() \
                or self.board.is_fifty_moves():
            pass  # Draw, scores remain [0.5, 0.5]
        return scores

    def is_valid_move(self, move, player):
        return self.board.is_legal(move)

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

    def copy(self):
        return self.board.copy()