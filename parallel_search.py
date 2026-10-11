from multiprocessing import Pool
from minimax import minimax


def evaluate_move(args):

    board, move, depth, maximizing = args

    captured = board.make_move(move)

    score = minimax(
        board,
        depth - 1,
        float("-inf"),
        float("inf"),
        not maximizing
    )

    board.undo_move(move, captured)

    return move, score


def analyze_moves(board, depth, color="white"):

    moves = board.generate_moves(color)

    if not moves:
        return []

    maximizing = color == "white"

    tasks = [
        (board, move, depth, maximizing)
        for move in moves
    ]

    with Pool() as pool:
        results = pool.map(
            evaluate_move,
            tasks
        )

    if maximizing:

        results.sort(
            key=lambda x: x[1],
            reverse=True
        )

    else:

        results.sort(
            key=lambda x: x[1]
        )

    return results


def parallel_search(board, depth, color="white"):

    results = analyze_moves(
        board,
        depth,
        color
    )

    if not results:
        return None, 0

    return results[0]

def get_best_line(board, depth, color, plies=4):

    line = []

    for _ in range(plies):

        results = analyze_moves(
            board,
            depth,
            color
        )

        if not results:
            break

        move, score = results[0]

        line.append(
            (move, score)
        )

        captured = board.make_move(
            move
        )

        color = (
            "black"
            if color == "white"
            else "white"
        )

    return line