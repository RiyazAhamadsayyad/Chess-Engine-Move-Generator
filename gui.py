import tkinter as tk
from tkinter import messagebox
import time

from board import Board
from parallel_search import parallel_search, analyze_moves


class ChessGUI:

    def __init__(self, root):

        self.root = root
        self.root.title("Chess Engine")
        self.root.geometry("1150x760")
        self.root.configure(bg="#111827")
        self.root.resizable(False, False)

        # Game state
        self.board = Board()
        self.selected = None
        self.valid_moves = []
        self.turn = "white"
        self.game_over = False
        self.last_move = None
        self.move_history = []

        self.depth = 3

        self.build_ui()
        self.draw_board()

    # =========================================================
    # BEST MOVE
    # =========================================================

    def show_best_move(self):

        if self.game_over:
            return

        if self.turn != "white":
            messagebox.showinfo(
                "Best Move",
                "Wait for the AI to complete its move."
            )
            return

        self.hint_button.config(
            state="disabled",
            text="ANALYZING..."
        )

        self.status_indicator.config(
            text="● ANALYZING POSITION",
            fg="#f59e0b"
        )

        self.search_label.config(
            text="Calculating..."
        )

        self.root.update()

        try:

            depth = int(
                self.depth_var.get()
            )

            start = time.perf_counter()

            results = analyze_moves(
                self.board,
                depth,
                "white"
            )

            end = time.perf_counter()

            if not results:

                messagebox.showinfo(
                    "Analysis",
                    "No moves available."
                )

                return

            best_move, best_score = results[0]

            # Highlight best move
            self.selected = best_move[0]

            self.valid_moves = [
                best_move[1]
            ]

            self.last_move = None

            # Statistics
            self.evaluation_label.config(
                text=f"{best_score / 100:.2f}"
            )

            self.time_label.config(
                text=f"{end - start:.3f} s"
            )

            self.best_move_label.config(
                text=self.format_move(best_move)
            )

            self.search_label.config(
                text="Analysis Complete"
            )

            self.draw_board()

            self.show_candidate_moves(
                results
            )

        except Exception as error:

            messagebox.showerror(
                "Analysis Error",
                str(error)
            )

        finally:

            self.hint_button.config(
                state="normal",
                text="BEST MOVE"
            )

            self.status_indicator.config(
                text="● ENGINE READY",
                fg="#22c55e"
            )

    # =========================================================
    # CANDIDATE MOVES
    # =========================================================

    def show_candidate_moves(self, results):

        self.history.delete(
            0,
            tk.END
        )

        self.history.insert(
            tk.END,
            "TOP CANDIDATE MOVES"
        )

        self.history.insert(
            tk.END,
            "------------------------------"
        )

        for index, (move, score) in enumerate(
            results[:5],
            start=1
        ):

            evaluation = score / 100

            if evaluation >= 0:
                score_text = f"+{evaluation:.2f}"
            else:
                score_text = f"{evaluation:.2f}"

            self.history.insert(
                tk.END,
                f"{index}. {self.format_move(move)}   {score_text}"
            )

    # =========================================================
    # BUILD UI
    # =========================================================

    def build_ui(self):

        # -----------------------------------------------------
        # Header
        # -----------------------------------------------------

        header = tk.Frame(
            self.root,
            bg="#111827",
            height=80
        )

        header.pack(
            fill="x"
        )

        title = tk.Label(
            header,
            text="♟  CHESS ENGINE",
            font=(
                "Segoe UI",
                24,
                "bold"
            ),
            fg="#f9fafb",
            bg="#111827"
        )

        title.pack(
            side="left",
            padx=30,
            pady=18
        )

        subtitle = tk.Label(
            header,
            text="MINIMAX  •  ALPHA-BETA  •  PARALLEL SEARCH",
            font=(
                "Segoe UI",
                10,
                "bold"
            ),
            fg="#94a3b8",
            bg="#111827"
        )

        subtitle.pack(
            side="left",
            padx=10
        )

        self.status_indicator = tk.Label(
            header,
            text="● ENGINE READY",
            font=(
                "Segoe UI",
                10,
                "bold"
            ),
            fg="#22c55e",
            bg="#111827"
        )

        self.status_indicator.pack(
            side="right",
            padx=30
        )

        # -----------------------------------------------------
        # Main
        # -----------------------------------------------------

        main = tk.Frame(
            self.root,
            bg="#111827"
        )

        main.pack(
            fill="both",
            expand=True,
            padx=25,
            pady=10
        )

        # -----------------------------------------------------
        # Chess Board
        # -----------------------------------------------------

        board_frame = tk.Frame(
            main,
            bg="#111827"
        )

        board_frame.pack(
            side="left",
            padx=(10, 30)
        )

        self.canvas = tk.Canvas(
            board_frame,
            width=640,
            height=640,
            bg="#111827",
            highlightthickness=0
        )

        self.canvas.pack()

        self.canvas.bind(
            "<Button-1>",
            self.on_click
        )

        # -----------------------------------------------------
        # Right Panel
        # -----------------------------------------------------

        self.panel = tk.Frame(
            main,
            width=380,
            height=640,
            bg="#1f2937"
        )

        self.panel.pack(
            side="right",
            fill="y"
        )

        self.panel.pack_propagate(
            False
        )

        self.create_panel()

        # -----------------------------------------------------
        # Footer
        # -----------------------------------------------------

        footer = tk.Frame(
            self.root,
            bg="#0f172a",
            height=45
        )

        footer.pack(
            fill="x",
            side="bottom"
        )

        footer_label = tk.Label(
            footer,
            text=(
                "● Alpha-Beta Enabled     "
                "● Multiprocessing Enabled     "
                "● Human vs AI"
            ),
            font=(
                "Segoe UI",
                10
            ),
            fg="#9ca3af",
            bg="#0f172a"
        )

        footer_label.pack(
            pady=12
        )

    # =========================================================
    # RIGHT PANEL
    # =========================================================

    def create_panel(self):

        title = tk.Label(
            self.panel,
            text="GAME STATUS",
            font=(
                "Segoe UI",
                15,
                "bold"
            ),
            fg="#f9fafb",
            bg="#1f2937"
        )

        title.pack(
            anchor="w",
            padx=25,
            pady=(20, 10)
        )

        # Turn
        self.turn_label = tk.Label(
            self.panel,
            text="White's Turn",
            font=(
                "Segoe UI",
                20,
                "bold"
            ),
            fg="#60a5fa",
            bg="#1f2937"
        )

        self.turn_label.pack(
            anchor="w",
            padx=25,
            pady=(0, 12)
        )

        # Mode
        mode_frame = tk.Frame(
            self.panel,
            bg="#1f2937"
        )

        mode_frame.pack(
            fill="x",
            padx=25,
            pady=3
        )

        tk.Label(
            mode_frame,
            text="Mode",
            font=(
                "Segoe UI",
                10
            ),
            fg="#d1d5db",
            bg="#1f2937"
        ).pack(
            side="left"
        )

        tk.Label(
            mode_frame,
            text="HUMAN vs AI",
            font=(
                "Segoe UI",
                10,
                "bold"
            ),
            fg="#22c55e",
            bg="#1f2937"
        ).pack(
            side="right"
        )

        # Search depth
        depth_frame = tk.Frame(
            self.panel,
            bg="#1f2937"
        )

        depth_frame.pack(
            fill="x",
            padx=25,
            pady=5
        )

        tk.Label(
            depth_frame,
            text="Search Depth",
            font=(
                "Segoe UI",
                11
            ),
            fg="#d1d5db",
            bg="#1f2937"
        ).pack(
            side="left"
        )

        self.depth_var = tk.StringVar(
            value="3"
        )

        depth_menu = tk.OptionMenu(
            depth_frame,
            self.depth_var,
            "1",
            "2",
            "3",
            "4"
        )

        depth_menu.configure(
            bg="#374151",
            fg="white",
            activebackground="#4b5563",
            activeforeground="white",
            highlightthickness=0
        )

        depth_menu["menu"].configure(
            bg="#374151",
            fg="white"
        )

        depth_menu.pack(
            side="right"
        )

        # -----------------------------------------------------
        # Statistics
        # -----------------------------------------------------

        stats_title = tk.Label(
            self.panel,
            text="ENGINE STATISTICS",
            font=(
                "Segoe UI",
                11,
                "bold"
            ),
            fg="#f9fafb",
            bg="#1f2937"
        )

        stats_title.pack(
            anchor="w",
            padx=25,
            pady=(10, 6)
        )

        # IMPORTANT
        # create_stat() uses self.stats_frame
        self.stats_frame = tk.Frame(
            self.panel,
            bg="#111827"
        )

        self.stats_frame.pack(
            fill="x",
            padx=25
        )

        self.evaluation_label = self.create_stat(
            "Evaluation",
            "+0.00"
        )

        self.time_label = self.create_stat(
            "Search Time",
            "0.00 s"
        )

        self.best_move_label = self.create_stat(
            "Best Move",
            "-"
        )

        self.search_label = self.create_stat(
            "Search",
            "Ready"
        )

        # -----------------------------------------------------
        # Best Move
        # -----------------------------------------------------

        self.hint_button = tk.Button(
            self.panel,
            text="BEST MOVE",
            command=self.show_best_move,
            font=(
                "Segoe UI",
                11,
                "bold"
            ),
            bg="#16a34a",
            fg="white",
            activebackground="#15803d",
            activeforeground="white",
            relief="flat",
            cursor="hand2",
            height=2
        )

        self.hint_button.pack(
            fill="x",
            padx=25,
            pady=(12, 5)
        )

        # -----------------------------------------------------
        # AI Move
        # -----------------------------------------------------

        self.ai_button = tk.Button(
            self.panel,
            text="AI MOVE",
            command=self.ai_move,
            font=(
                "Segoe UI",
                11,
                "bold"
            ),
            bg="#2563eb",
            fg="white",
            activebackground="#1d4ed8",
            activeforeground="white",
            relief="flat",
            cursor="hand2",
            height=2
        )

        self.ai_button.pack(
            fill="x",
            padx=25,
            pady=5
        )

        # -----------------------------------------------------
        # New Game
        # -----------------------------------------------------

        reset_button = tk.Button(
            self.panel,
            text="NEW GAME",
            command=self.new_game,
            font=(
                "Segoe UI",
                11,
                "bold"
            ),
            bg="#374151",
            fg="white",
            activebackground="#4b5563",
            activeforeground="white",
            relief="flat",
            cursor="hand2",
            height=2
        )

        reset_button.pack(
            fill="x",
            padx=25,
            pady=5
        )

        # -----------------------------------------------------
        # Move History
        # -----------------------------------------------------

        tk.Label(
            self.panel,
            text="MOVE HISTORY / ANALYSIS",
            font=(
                "Segoe UI",
                11,
                "bold"
            ),
            fg="#f9fafb",
            bg="#1f2937"
        ).pack(
            anchor="w",
            padx=25,
            pady=(12, 6)
        )

        self.history = tk.Listbox(
            self.panel,
            bg="#111827",
            fg="#d1d5db",
            font=(
                "Consolas",
                10
            ),
            relief="flat",
            highlightthickness=0
        )

        self.history.pack(
            fill="both",
            expand=True,
            padx=25,
            pady=(0, 15)
        )

    # =========================================================
    # STATISTICS
    # =========================================================

    def create_stat(
        self,
        name,
        value
    ):

        frame = tk.Frame(
            self.stats_frame,
            bg="#111827"
        )

        frame.pack(
            fill="x"
        )

        tk.Label(
            frame,
            text=name,
            font=(
                "Segoe UI",
                9
            ),
            fg="#94a3b8",
            bg="#111827"
        ).pack(
            side="left",
            padx=10,
            pady=6
        )

        label = tk.Label(
            frame,
            text=value,
            font=(
                "Segoe UI",
                9,
                "bold"
            ),
            fg="#f8fafc",
            bg="#111827"
        )

        label.pack(
            side="right",
            padx=10
        )

        return label

    # =========================================================
    # DRAW BOARD
    # =========================================================

    def draw_board(self):

        self.canvas.delete(
            "all"
        )

        size = 80

        light = "#f0d9b5"
        dark = "#b58863"

        for row in range(8):

            for col in range(8):

                x1 = col * size
                y1 = row * size

                x2 = x1 + size
                y2 = y1 + size

                color = (
                    light
                    if (row + col) % 2 == 0
                    else dark
                )

                self.canvas.create_rectangle(
                    x1,
                    y1,
                    x2,
                    y2,
                    fill=color,
                    outline=""
                )

                # Last move
                if self.last_move:

                    if (
                        (row, col)
                        == self.last_move[0]
                        or
                        (row, col)
                        == self.last_move[1]
                    ):

                        self.canvas.create_rectangle(
                            x1,
                            y1,
                            x2,
                            y2,
                            fill="#d4a72c",
                            stipple="gray50",
                            outline=""
                        )

                # Valid / recommended move
                if (
                    row,
                    col
                ) in self.valid_moves:

                    self.canvas.create_oval(
                        x1 + 30,
                        y1 + 30,
                        x2 - 30,
                        y2 - 30,
                        fill="#22c55e",
                        outline=""
                    )

                # Piece
                piece = self.board.board[
                    row
                ][
                    col
                ]

                if piece:

                    symbol = self.get_symbol(
                        piece
                    )

                    # Shadow
                    self.canvas.create_text(
                        x1 + 42,
                        y1 + 43,
                        text=symbol,
                        font=(
                            "Segoe UI Symbol",
                            48
                        ),
                        fill="#000000"
                    )

                    # Piece
                    piece_color = (
                        "#ffffff"
                        if piece.color == "white"
                        else "#111827"
                    )

                    self.canvas.create_text(
                        x1 + 40,
                        y1 + 40,
                        text=symbol,
                        font=(
                            "Segoe UI Symbol",
                            48
                        ),
                        fill=piece_color
                    )

        # Selected / best-move square
        if self.selected:

            row, col = self.selected

            self.canvas.create_rectangle(
                col * size + 3,
                row * size + 3,
                col * size + 77,
                row * size + 77,
                outline="#facc15",
                width=5
            )

    # =========================================================
    # CHESS SYMBOLS
    # =========================================================

    def get_symbol(
        self,
        piece
    ):

        symbols = {

            "white": {
                "Pawn": "♙",
                "Knight": "♘",
                "Bishop": "♗",
                "Rook": "♖",
                "Queen": "♕",
                "King": "♔"
            },

            "black": {
                "Pawn": "♟",
                "Knight": "♞",
                "Bishop": "♝",
                "Rook": "♜",
                "Queen": "♛",
                "King": "♚"
            }
        }

        return symbols[
            piece.color
        ][
            piece.__class__.__name__
        ]

    # =========================================================
    # HUMAN CLICK
    # =========================================================

    def on_click(
        self,
        event
    ):

        # Human controls White
        if (
            self.turn != "white"
            or
            self.game_over
        ):
            return

        col = event.x // 80
        row = event.y // 80

        if not (
            0 <= row < 8
            and
            0 <= col < 8
        ):
            return

        piece = self.board.board[
            row
        ][
            col
        ]

        # -----------------------------------------------------
        # Select piece
        # -----------------------------------------------------

        if self.selected is None:

            if (
                piece is not None
                and
                piece.color == "white"
            ):

                self.selected = (
                    row,
                    col
                )

                all_moves = (
                    self.board.generate_moves(
                        "white"
                    )
                )

                self.valid_moves = [
                    move[1]
                    for move in all_moves
                    if move[0]
                    == self.selected
                ]

                self.draw_board()

            return

        # -----------------------------------------------------
        # Destination
        # -----------------------------------------------------

        target = (
            row,
            col
        )

        # -----------------------------------------------------
        # Make move
        # -----------------------------------------------------

        if target in self.valid_moves:

            move = (
                self.selected,
                target
            )

            self.board.make_move(
                move
            )

            self.last_move = move

            self.add_history(
                move,
                "White"
            )

            self.selected = None

            self.valid_moves = []

            self.turn = "black"

            self.turn_label.config(
                text="Black's Turn",
                fg="#f87171"
            )

            self.status_indicator.config(
                text="● AI THINKING",
                fg="#f59e0b"
            )

            self.draw_board()

            # Automatically make AI move
            self.root.after(
                250,
                self.ai_move
            )

        else:

            # Select another White piece
            if (
                piece is not None
                and
                piece.color == "white"
            ):

                self.selected = (
                    row,
                    col
                )

                all_moves = (
                    self.board.generate_moves(
                        "white"
                    )
                )

                self.valid_moves = [
                    move[1]
                    for move in all_moves
                    if move[0]
                    == self.selected
                ]

            else:

                self.selected = None
                self.valid_moves = []

            self.draw_board()

    # =========================================================
    # AI MOVE
    # =========================================================

    def ai_move(self):

        if (
            self.turn != "black"
            or
            self.game_over
        ):
            return

        self.ai_button.config(
            state="disabled",
            text="THINKING..."
        )

        self.hint_button.config(
            state="disabled"
        )

        self.status_indicator.config(
            text="● AI THINKING",
            fg="#f59e0b"
        )

        self.search_label.config(
            text="Searching..."
        )

        self.root.update()

        try:

            depth = int(
                self.depth_var.get()
            )

            start = time.perf_counter()

            # IMPORTANT:
            # AI searches Black moves
            move, score = parallel_search(
                self.board,
                depth,
                "black"
            )

            end = time.perf_counter()

            if move is None:

                self.game_over = True

                messagebox.showinfo(
                    "Game Over",
                    "AI has no available moves."
                )

                return

            self.board.make_move(
                move
            )

            self.last_move = move

            self.add_history(
                move,
                "Black"
            )

            self.evaluation_label.config(
                text=f"{score / 100:.2f}"
            )

            self.time_label.config(
                text=f"{end - start:.3f} s"
            )

            self.best_move_label.config(
                text=self.format_move(
                    move
                )
            )

            self.search_label.config(
                text="Completed"
            )

            self.selected = None

            self.valid_moves = []

            self.turn = "white"

            self.turn_label.config(
                text="White's Turn",
                fg="#60a5fa"
            )

            self.status_indicator.config(
                text="● ENGINE READY",
                fg="#22c55e"
            )

            self.draw_board()

        except TypeError:

            messagebox.showerror(
                "Engine Error",
                "Update parallel_search.py so that it supports:\n\n"
                "parallel_search(board, depth, color)"
            )

        except Exception as error:

            messagebox.showerror(
                "AI Error",
                str(error)
            )

        finally:

            self.ai_button.config(
                state="normal",
                text="AI MOVE"
            )

            self.hint_button.config(
                state="normal"
            )

    # =========================================================
    # MOVE HISTORY
    # =========================================================

    def add_history(
        self,
        move,
        player
    ):

        text = self.format_move(
            move
        )

        self.move_history.append(
            (player, text)
        )

        move_number = (
            len(self.move_history) + 1
        ) // 2

        if player == "White":

            display = (
                f"{move_number}. {text}"
            )

        else:

            display = (
                f"{move_number}... {text}"
            )

        self.history.insert(
            tk.END,
            display
        )

        self.history.see(
            tk.END
        )

    # =========================================================
    # FORMAT MOVE
    # =========================================================

    def format_move(
        self,
        move
    ):

        start, end = move

        files = "abcdefgh"

        start_text = (
            files[start[1]]
            +
            str(8 - start[0])
        )

        end_text = (
            files[end[1]]
            +
            str(8 - end[0])
        )

        return (
            f"{start_text} → {end_text}"
        )

    # =========================================================
    # NEW GAME
    # =========================================================

    def new_game(self):

        self.board = Board()

        self.selected = None

        self.valid_moves = []

        self.last_move = None

        self.turn = "white"

        self.game_over = False

        self.move_history = []

        self.history.delete(
            0,
            tk.END
        )

        self.turn_label.config(
            text="White's Turn",
            fg="#60a5fa"
        )

        self.status_indicator.config(
            text="● ENGINE READY",
            fg="#22c55e"
        )

        self.evaluation_label.config(
            text="+0.00"
        )

        self.time_label.config(
            text="0.00 s"
        )

        self.best_move_label.config(
            text="-"
        )

        self.search_label.config(
            text="Ready"
        )

        self.ai_button.config(
            state="normal",
            text="AI MOVE"
        )

        self.hint_button.config(
            state="normal",
            text="BEST MOVE"
        )

        self.draw_board()


if __name__ == "__main__":

    root = tk.Tk()

    app = ChessGUI(
        root
    )

    root.mainloop()