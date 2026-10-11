class Piece:
    def __init__(self, color):
        self.color = color

    def get_moves(self, board, row, col):
        return []


class Pawn(Piece):

    def get_moves(self, board, row, col):

        moves = []

        direction = -1 if self.color == "white" else 1

        new_row = row + direction

        if 0 <= new_row < 8:

            if board[new_row][col] is None:
                moves.append((new_row, col))

                start_row = 6 if self.color == "white" else 1

                double_row = row + 2 * direction

                if row == start_row and board[double_row][col] is None:
                    moves.append((double_row, col))

        for dc in (-1, 1):

            new_col = col + dc

            if 0 <= new_row < 8 and 0 <= new_col < 8:

                target = board[new_row][new_col]

                if target is not None and target.color != self.color:
                    moves.append((new_row, new_col))

        return moves


class Knight(Piece):
    def get_moves(self, board, row, col):
        moves = []

        directions = [
            (-2, -1), (-2, 1),
            (-1, -2), (-1, 2),
            (1, -2), (1, 2),
            (2, -1), (2, 1)
        ]

        for dr, dc in directions:
            r = row + dr
            c = col + dc

            if 0 <= r < 8 and 0 <= c < 8:
                if board[r][c] is None or board[r][c].color != self.color:
                    moves.append((r, c))

        return moves


class Bishop(Piece):
    def get_moves(self, board, row, col):
        return sliding_moves(
            board, row, col, self.color,
            [(-1, -1), (-1, 1), (1, -1), (1, 1)]
        )


class Rook(Piece):
    def get_moves(self, board, row, col):
        return sliding_moves(
            board, row, col, self.color,
            [(-1, 0), (1, 0), (0, -1), (0, 1)]
        )


class Queen(Piece):
    def get_moves(self, board, row, col):
        return sliding_moves(
            board, row, col, self.color,
            [
                (-1, -1), (-1, 1),
                (1, -1), (1, 1),
                (-1, 0), (1, 0),
                (0, -1), (0, 1)
            ]
        )


class King(Piece):
    def get_moves(self, board, row, col):
        moves = []

        directions = [
            (-1, -1), (-1, 0), (-1, 1),
            (0, -1), (0, 1),
            (1, -1), (1, 0), (1, 1)
        ]

        for dr, dc in directions:
            r = row + dr
            c = col + dc

            if 0 <= r < 8 and 0 <= c < 8:
                if board[r][c] is None or board[r][c].color != self.color:
                    moves.append((r, c))

        return moves


def sliding_moves(board, row, col, color, directions):
    moves = []

    for dr, dc in directions:
        r = row + dr
        c = col + dc

        while 0 <= r < 8 and 0 <= c < 8:

            if board[r][c] is None:
                moves.append((r, c))

            else:
                if board[r][c].color != color:
                    moves.append((r, c))
                break

            r += dr
            c += dc

    return moves
