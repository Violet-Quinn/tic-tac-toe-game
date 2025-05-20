# Tic Tac Toe Game in Python

This project is a simple, text-based version of the classic Tic Tac Toe game built using Python. It allows two players to take turns placing Xs and Os on a 3x3 grid via the terminal. The game is entirely console-driven and focuses on core programming logic without any external libraries.

---

## 🎮 Features

- **Two-Player Turn-Based Gameplay**: Player X and Player O alternate turns, entering positions via the keyboard.
- **Input Validation**: Ensures players can only enter numbers between 0 and 8 and only into empty cells. Invalid inputs prompt error messages.
- **Win Detection**: The game checks all possible win conditions (rows, columns, diagonals) after each move.
- **Tie Detection**: Declares a tie when the board is full and no player has won.
- **Simple UI**: The current board state is printed after each move in a clear, easy-to-read 3x3 format.

---

## 🧠 How to Play

- The game uses a **0-8** index system representing the 9 grid positions as follows:

```
0 | 1 | 2
--+---+--
3 | 4 | 5
--+---+--
6 | 7 | 8
```

- Players are prompted to enter the position number during their turn.
- The game continues until a player wins or all positions are filled (resulting in a tie).

---

## ▶️ Running the Game

To run the game, simply execute the Python script:

```bash
python tic_tac_toe.py
```

No external dependencies are required — it runs with standard Python.
