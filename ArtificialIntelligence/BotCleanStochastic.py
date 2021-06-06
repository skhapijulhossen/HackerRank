#!/bin/python3

def nextMove(posr, posc, board):
    dirtyCell = []
    for row in range(5):
        for col in range(5):
            if board[row][col] == 'd':
                dirtyCell = [row,col]
                break 
    move=''
    if dirtyCell[1] < posc:
        move='LEFT'
    elif dirtyCell[1] > posc:
        move='RIGHT'
    elif dirtyCell[0] < posr:
        move='UP'
    elif dirtyCell[0] > posr:
        move='DOWN'
    else:
        move='CLEAN'
    print(move)

if __name__ == "__main__":
    pos = [int(i) for i in input().strip().split()]
    board = [[j for j in input().strip()] for i in range(5)]
    nextMove(pos[0], pos[1], board)