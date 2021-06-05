#!/usr/bin/python

# Head ends here

def next_move(posr, posc, board):
    dirtyCells = []
    for row in range(5):
        dirtyCells.extend([{(abs(posr-row)+abs(posc-col)): (row, col)}
                           for col in range(5) if board[row][col] == "d"])
    nearest = list(sorted(dirtyCells, key=lambda k: list(k.keys())[0])[0].values())
    step=''
    print(nearest)
    if nearest[0][0] == posr:
        if nearest[0][1] < posc:
            step = "LEFT"
        elif nearest[0][1] > posc:
            step = "RIGHT"
        else:
            pass
    else:
        if nearest[0][0] < posr:
            step = "UP"
        elif nearest[0][0] > posr:
            step = "DOWN"
        else:
            pass
    print(step)
        



    

# Tail starts here


if __name__ == "__main__":
    pos = [int(i) for i in input().strip().split()]
    board = [[j for j in input().strip()] for i in range(5)]
    next_move(pos[0], pos[1], board)
