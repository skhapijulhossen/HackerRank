#!/usr/bin/python
from math import sqrt
# Head ends here

def next_move(posr, posc, board):
    dirtyCells = []
    for row in range(5):
        dirtyCells.extend([{sqrt(((posr-row)**2)+((posc-col)**2)): (row, col)}
                           for col in range(5) if board[row][col] == "d"])
    nearest = list(sorted(dirtyCells, key=lambda k: list(k.keys())[0])[0].values())
    move=''
    if nearest[0][1] < posc:
        move='LEFT'
    elif nearest[0][1] > posc:
        move='RIGHT'
    elif nearest[0][0] < posr:
        move='UP'
    elif nearest[0][0] > posr:
        move='DOWN'
    else:
        move='CLEAN'
    print(move)

# Tail starts here


if __name__ == "__main__":
    pos = [int(i) for i in input().strip().split()]
    board = [[j for j in input().strip()] for i in range(5)]
    next_move(pos[0], pos[1], board)
