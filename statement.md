# Project Statement - Tic Tac Toe in Python

## Problem statement

Tic Tac Toe is a simple game, but writing it as a program means dealing with a lot of basic programming ideas at once: storing the board, taking turns, checking every way to win, and making sure the program doesn't break when someone types something wrong. A lot of simple versions online just crash on bad input.

The aim of this project is to build a Tic Tac Toe game that runs in the terminal, lets two people play or one person play against the computer, follows all the rules, and handles wrong input properly, with the code split into small functions that are easy to read.

## Scope of the project

In scope:
- A 3 x 3 Tic Tac Toe game played in the terminal
- Two modes: two players on one computer, and one player against the computer
- A simple computer opponent that wins when it can, blocks the player, and takes the centre
- Checking every input and asking again if it's wrong
- Keeping the score over many rounds

Not in scope:
- A graphical window (the game is text only)
- Playing online or over a network
- Bigger boards like 4 x 4
- Saving scores after the game is closed
- An unbeatable computer (it follows simple rules, so it can be beaten)

## Target users

- Students and beginners who want to play a quick game in the terminal
- Beginners learning Python, who can read the code to see how a small game is built with functions
- Teachers or evaluators who want to run the project from the command line

## High-level features

1. Game mode menu: choose 2 players or play against the computer
2. Board display: the board with numbers 1 to 9 in the free boxes
3. Player input and validation: only accepts a free box from 1 to 9
4. Win and draw checking: rows, columns and diagonals
5. Computer opponent: win, block, centre, or a random free box
6. Score: the score is shown after every round, and you can play again
