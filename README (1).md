# ♟️ Chess Engine Move Generator

A Python-based simplified chess engine that generates chess moves, evaluates board positions, and finds the best move using **Minimax with Alpha-Beta Pruning**. The project also uses **Object-Oriented Programming (OOP)** and **Multiprocessing** for parallel move evaluation.

## 📌 Project Overview

The main objective is to develop a simplified chess engine capable of:
- Generating possible chess moves
- Evaluating chess board positions
- Searching for the best move
- Using Minimax for decision making
- Improving search using Alpha-Beta Pruning
- Using multiprocessing for parallel move evaluation
- Providing a Human vs AI graphical interface

## 🎯 Problem Statement

**Generate legal moves and evaluate positions for a simplified chess engine.**

The project uses Minimax, Alpha-Beta Pruning, board evaluation, and parallel processing to search possible moves efficiently.

## 🎯 Objectives

1. Develop a chess board representation using Python.
2. Implement chess pieces using OOP.
3. Generate possible moves for each piece.
4. Evaluate board positions.
5. Implement Minimax search.
6. Improve Minimax using Alpha-Beta Pruning.
7. Use multiprocessing for parallel move evaluation.
8. Develop a Human vs AI chess interface.
9. Display AI move suggestions and search information.

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python | Main programming language |
| OOP | Chess piece and board design |
| Minimax | AI decision making |
| Alpha-Beta Pruning | Reduce unnecessary search |
| Multiprocessing | Parallel move evaluation |
| Tkinter | Graphical User Interface |
| PyCharm | Development environment |
| Git & GitHub | Version control |

## 🧠 Algorithms Used

### 1. Move Generation

```text
Current Position
       ↓
Find Player Pieces
       ↓
Generate Possible Moves
       ↓
Evaluate Moves
```

### 2. Minimax

Minimax selects a move by considering the AI's moves and the opponent's possible responses.

```text
              Current Position
                     |
          -----------------------
          |          |          |
        Move 1     Move 2     Move 3
          |          |          |
       Opponent   Opponent   Opponent
        Moves      Moves      Moves
          |          |          |
       Evaluate   Evaluate   Evaluate
```

### 3. Alpha-Beta Pruning

Alpha-Beta Pruning removes branches that cannot affect the final decision.

```text
Minimax
   ↓
Alpha-Beta Pruning
   ↓
Ignore unnecessary branches
   ↓
Faster search
```

### 4. Multiprocessing

Different candidate moves can be evaluated in parallel.

```text
                 Available Moves
                       |
          ---------------------------
          |            |            |
        Move A       Move B       Move C
          |            |            |
       Process 1    Process 2    Process 3
          |            |            |
          -------- Evaluation -------
                       |
                  Best Move
```

## 🏗️ Project Architecture

```text
                    Chess Engine
                         |
        ---------------------------------
        |               |               |
    Board System     AI Search       GUI
        |               |               |
   Move Generation   Minimax        Tkinter
        |               |
   Chess Pieces    Alpha-Beta
                        |
                  Multiprocessing
```

## 📂 Project Structure

```text
CTP PROJECT/
│
├── board.py
├── evaluator.py
├── main.py
├── minimax.py
├── move.py
├── parallel_search.py
├── pieces.py
├── gui.py
├── README.md
├── .gitignore
│
└── .venv/
```

| File | Description |
|---|---|
| `board.py` | Creates and manages the chess board |
| `pieces.py` | Defines chess pieces and movement |
| `move.py` | Handles move-related functionality |
| `evaluator.py` | Evaluates board positions |
| `minimax.py` | Implements Minimax and Alpha-Beta search |
| `parallel_search.py` | Performs parallel move evaluation |
| `gui.py` | Provides the graphical chess interface |
| `main.py` | Starts the application |
| `README.md` | Project documentation |
| `.gitignore` | Prevents unnecessary files from being uploaded |

## ♟️ Chess Pieces

The project represents:
- Pawn
- Knight
- Bishop
- Rook
- Queen
- King

Each piece is represented as an object with its own movement logic.

## 💻 How to Run

### 1. Clone the Repository

```bash
git clone https://github.com/RiyazAhamadsyadav/Chess-Engine-Move-Generator.git
cd Chess-Engine-Move-Generator
```

### 2. Create a Virtual Environment

```bash
python -m venv .venv
```

### 3. Activate the Virtual Environment

**Windows:**
```bash
.venv\Scripts\activate
```

**Linux/macOS:**
```bash
source .venv/bin/activate
```

### 4. Tkinter on Ubuntu

```bash
sudo apt install python3-tk
```

### 5. Run the Application

```bash
python main.py
```

## 🎮 How to Play

1. Start `main.py`.
2. The human player controls the White pieces.
3. Select a white piece.
4. Select a valid destination square.
5. The move is executed.
6. The AI automatically searches for a Black move.
7. The AI selects its best move based on the configured search depth.

## 🤖 AI Move Selection

```text
Human Move
    ↓
Update Board
    ↓
Generate AI Moves
    ↓
Evaluate Candidate Moves
    ↓
Minimax Search
    ↓
Alpha-Beta Pruning
    ↓
Compare Scores
    ↓
Select Best Move
    ↓
Update Board
```

## 🔎 Search Depth

A higher depth allows the AI to look further ahead but requires more computation.

```text
Depth 1 → Immediate moves
Depth 2 → Move + opponent response
Depth 3 → Several moves ahead
Higher Depth → Stronger search, more computation
```

The engine searches the game tree up to the configured depth; it does not calculate every possible chess game.

## 📊 Board Evaluation

A simplified evaluation can consider:
- Material value
- Captured pieces
- Position advantage
- Available moves

Example piece values:

```text
Pawn   = 1
Knight = 3
Bishop = 3
Rook   = 5
Queen  = 9
King   = Very High
```

## 🖥️ Graphical User Interface

The Tkinter GUI provides:
- Chess board
- Human vs AI gameplay
- Game status
- Search depth
- Position evaluation
- Search time
- Best move
- AI move information
- Move history
- New Game option

## ⭐ Key Features

- Chess board representation
- Multiple chess piece classes
- Minimax AI
- Alpha-Beta Pruning
- Parallel move evaluation
- Tkinter graphical interface
- Human vs AI gameplay
- Best move analysis
- Board evaluation
- New game functionality
- Modular Python structure

## 🔬 OOP Concepts Used

### Classes
Chess pieces are implemented as classes.

```python
class Pawn:
    ...
```

### Objects

```python
Pawn("white")
```

### Encapsulation
Piece movement logic is organized inside the corresponding classes.

### Inheritance
Different chess pieces can share common behavior through a common design.

### Polymorphism
Different pieces can implement their own movement rules while being handled through a common interface.

## ⚡ Advantages

- Modular and easy to understand
- Demonstrates practical AI search
- Alpha-Beta Pruning reduces unnecessary computation
- Supports parallel evaluation
- Provides an interactive GUI
- Demonstrates OOP concepts
- Can be extended into a stronger chess engine

## ⚠️ Limitations

This is a **simplified chess engine**, not a tournament-level engine.

Possible limitations:
- Limited search depth
- Simplified evaluation function
- Search performance depends on hardware
- Some advanced chess rules may require additional implementation
- Not equivalent to professional engines such as Stockfish

## 🚀 Future Enhancements

- Checkmate detection
- Stalemate detection
- Castling
- En passant
- Pawn promotion
- Improved evaluation function
- Transposition tables
- Opening book
- Iterative deepening
- Move ordering
- Stronger AI
- Difficulty levels
- Stockfish comparison
- Online multiplayer
- Game saving and loading

## 📚 Learning Outcomes

- Python programming
- Object-Oriented Programming
- Data structures
- Chess move generation
- Game tree search
- Minimax algorithm
- Alpha-Beta Pruning
- Parallel processing
- GUI development
- Software modularization
- Git and GitHub version control

## 👨‍💻 Author

**Riyaz Ahamad**

GitHub: https://github.com/RiyazAhamadsyadav

## 📜 License

This project is developed for educational and academic purposes.

## ⭐ Project Summary

**Chess Engine Move Generator** is a Python-based simplified chess engine that combines **Object-Oriented Programming, Minimax, Alpha-Beta Pruning, and Multiprocessing** to generate and evaluate chess moves.

The project also provides a **Human vs AI graphical interface**, allowing users to play against the engine and observe its move-search process.
