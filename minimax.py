from evaluator import evaluate


def minimax(board, depth, alpha, beta, maximizing):

    if depth == 0:
        return evaluate(board)

    color = "white" if maximizing else "black"

    moves = board.generate_moves(color)

    if not moves:
        return evaluate(board)

    if maximizing:

        best = float("-inf")

        for move in moves:

            captured = board.make_move(move)

            score = minimax(
                board,
                depth - 1,
                alpha,
                beta,
                False
            )

            board.undo_move(move, captured)

            best = max(best, score)

            alpha = max(alpha, best)

            if beta <= alpha:
                break

        return best

    else:

        best = float("inf")

        for move in moves:

            captured = board.make_move(move)

            score = minimax(
                board,
                depth - 1,
                alpha,
                beta,
                True
            )

            board.undo_move(move, captured)

            best = min(best, score)

            beta = min(beta, best)

            if beta <= alpha:
                break

        return best


def find_best_move(board, depth):

    best_move = None
    best_score = float("-inf")

    moves = board.generate_moves("white")

    for move in moves:

        captured = board.make_move(move)

        score = minimax(
            board,
            depth - 1,
            float("-inf"),
            float("inf"),
            False
        )

        board.undo_move(move, captured)

        if score > best_score:
            best_score = score
            best_move = move

    return best_move, best_score