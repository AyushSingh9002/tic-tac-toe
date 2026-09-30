# Tic Tac Toe in Python

## Overview

This is a Tic Tac Toe game I made in Python for my VITyarthi course project. It runs in the terminal, so you play it by typing numbers. You can play with a friend on the same computer, or play against the computer.

The whole game is in one file, `tic tac toe2.py`. The code is split into 10 small functions, and each one does one job, like showing the board, checking for a win or picking the computer's move.

## Features

- Two modes: 2 players, or play against the computer
- The board shows numbers 1 to 9 in the empty boxes, so you know what to type
- Wrong input is handled. If you type a letter, a number outside 1 to 9, or a box that is already used, it tells you and asks again
- Checks for a win (row, column or diagonal) and for a draw
- The computer tries to win first, then blocks you, then takes the centre
- Keeps the score so you can play many rounds

## Technologies used

- Python 3
- The built-in `random` module (for the computer's moves)
- Git and GitHub for version control
- VS Code as the editor

## Project files

```
tic-tac-toe/
├── tic tac toe2.py    the full game
├── README.md          this file
└── statement.md       problem statement and scope
```

## How to install and run

You only need Python 3. Nothing else has to be installed.

1. Check that Python is installed. Open a terminal and type:

```
python3 --version
```

On Windows use `python` instead of `python3` in all the commands.

2. Download the project and go into the folder:

```
git clone https://github.com/AyushSingh9002/tic-tac-toe.git
cd tic-tac-toe
```

(Or on GitHub click Code > Download ZIP, unzip it and open a terminal in that folder.)

3. Start the game:

```
python3 "tic tac toe2.py"
```

Keep the quotes, because the file name has spaces in it. There is nothing to configure. The game starts straight away.

## How to play

1. Type 1 for 2 players, or 2 to play against the computer
2. X always plays first. Against the computer you are X
3. On your turn type a number from 1 to 9 and press Enter:

```
 1 | 2 | 3
---+---+---
 4 | 5 | 6
---+---+---
 7 | 8 | 9
```

4. Get 3 in a line to win. If all 9 boxes fill up with no winner, it's a draw
5. After each round type y to play again, or anything else to stop

## How to test it

The game is tested by playing it and trying these cases:

| What to try | What should happen |
| --- | --- |
| Type a letter like `abc` | "Please type a number from 1 to 9." and it asks again |
| Type `0` or `10` | "Please type a number from 1 to 9." and it asks again |
| Pick a box that is already taken | "That spot is already taken. Try another one." |
| Get 3 in a row, column or diagonal | "Player X wins!" (or O) and the score goes up |
| Fill all 9 boxes with no winner | "It's a draw!" |
| Against the computer, put X on 1 and 2 | The computer blocks you on 3 |
| Type `3` in the mode menu | "Please enter 1 or 2." |
| Type `y` after a round | A new round starts and the score is kept |

## Screenshots

A game against the computer:

```
 X | X | O
---+---+---
 4 | O | X
---+---+---
 7 | 8 | 9

Computer chooses position 7

 X | X | O
---+---+---
 4 | O | X
---+---+---
 O | 8 | 9

The computer wins!

Score -> X: 0 | O: 1 | Draws: 0
Play again? (y/n):
```
