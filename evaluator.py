PIECE_VALUES = {
    "Pawn": 100,
    "Knight": 320,
    "Bishop": 330,
    "Rook": 500,
    "Queen": 900,
    "King": 20000
}


def evaluate(board):

    score = 0

    for row in board.board:

        for piece in row:

            if piece is not None:

                value = PIECE_VALUES[
                    piece.__class__.__name__
                ]

                if piece.color == "white":
                    score += value
                else:
                    score -= value

    return score