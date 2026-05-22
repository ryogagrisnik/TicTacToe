# Tic Tac Toe

A two-player tic-tac-toe game built from scratch in Python using the turtle graphics library. My first Python game project!

## How to play

1. Run the game:
2. 2. A turtle graphics window opens with a 3×3 grid.
3. Players take turns clicking on empty cells:
   - **Player 1** places **X** (blue) on odd rounds
   - **Player 2** places **O** (red) on even rounds
4. First player to get 3 in a row (horizontally, vertically, or diagonally) wins!
5. If all 9 cells fill up with no winner, the game ends in a tie.

## Features

- Click-to-play interface using turtle's event handling
- Automatic turn switching between X and O
- Detects all 8 winning combinations (3 rows, 3 columns, 2 diagonals)
- Tie detection when the board fills up
- Game locks after a win or tie so no more marks can be placed

## Built with

- Python 3
- `turtle` (Python standard library — no extra installs needed)

## What I learned

- Event-driven programming with `onscreenclick`
- Managing game state with global variables
- Grid math (converting click coordinates to row/column with `//` and `%`)
- Debugging Python scoping issues (the joys of `global`)
- Using lists of lists to track 2D state
