from pieces import Pawn, Knight, Bishop, Rook, Queen, King


class Board:

    def __init__(self):
        self.board = self.create_board()

    def create_board(self):

        board = [[None for _ in range(8)] for _ in range(8)]

        board[0] = [
            Rook("black"),
            Knight("black"),
            Bishop("black"),
            Queen("black"),
            King("black"),
            Bishop("black"),
            Knight("black"),
            Rook("black")
        ]

        board[1] = [
            Pawn("black") for _ in range(8)
        ]

        board[6] = [
            Pawn("white") for _ in range(8)
        ]

        board[7] = [
            Rook("white"),
            Knight("white"),
            Bishop("white"),
            Queen("white"),
            King("white"),
            Bishop("white"),
            Knight("white"),
            Rook("white")
        ]

        return board

    def display(self):

        print("\n  a b c d e f g h")

        for row in range(8):

            print(8 - row, end=" ")

            for col in range(8):

                piece = self.board[row][col]

                if piece is None:
                    print(".", end=" ")

                else:
                    symbol = piece.__class__.__name__[0]

                    if piece.color == "white":
                        print(symbol.upper(), end=" ")
                    else:
                        print(symbol.lower(), end=" ")

            print(8 - row)

        print("  a b c d e f g h")

    def generate_moves(self, color):

        moves = []

        for row in range(8):

            for col in range(8):

                piece = self.board[row][col]

                if piece is not None and piece.color == color:

                    destinations = piece.get_moves(
                        self.board,
                        row,
                        col
                    )

                    for destination in destinations:
                        moves.append(
                            ((row, col), destination)
                        )

        return moves

    def make_move(self, move):

        start, end = move

        piece = self.board[start[0]][start[1]]

        captured = self.board[end[0]][end[1]]

        self.board[end[0]][end[1]] = piece

        self.board[start[0]][start[1]] = None

        return captured

    def undo_move(self, move, captured):

        start, end = move

        piece = self.board[end[0]][end[1]]

        self.board[start[0]][start[1]] = piece

        self.board[end[0]][end[1]] = captured

    def find_king(self, color):

        for row in range(8):

            for col in range(8):

                piece = self.board[row][col]

                if (
                        piece is not None
                        and piece.color == color
                        and isinstance(piece, King)
                ):
                    return row, col

        return None

    def is_square_attacked(self, row, col, attacker_color):

        moves = self.generate_moves(attacker_color)

        for move in moves:

            if move[1] == (row, col):
                return True

        return False

    def is_in_check(self, color):

        king_position = self.find_king(color)

        if king_position is None:
            return True

        opponent = "black" if color == "white" else "white"

        return self.is_square_attacked(
            king_position[0],
            king_position[1],
            opponent
        )
