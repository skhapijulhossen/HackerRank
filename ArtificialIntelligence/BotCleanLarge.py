from math import sqrt

def next_move(posx, posy, dimx, dimy, board):
    dirtyCells = []
    posr,posc = posx, posy
    if board[posx][posy] == 'd':
        print('CLEAN')
        return
    for row in range(dimx):
        dirtyCells.extend([{sqrt(((posx-row)**2)+((posy-col)**2)): (row, col)}
                           for col in range(dimy) if board[row][col] == "d"])
    nearest = list(sorted(dirtyCells, key=lambda k: list(k.keys())[0])[0].values())
    move=''
    if nearest[0][1] < posy:
        move='LEFT'
    elif nearest[0][1] > posy:
        move='RIGHT'
    elif nearest[0][0] < posx:
        move='UP'
    elif nearest[0][0] > posx:
        move='DOWN'
    else:
        move='CLEAN'
    print(move)

if __name__ == "__main__":
    pos = [int(i) for i in input().strip().split()]
    dim = [int(i) for i in input().strip().split()]
    board = [[j for j in input().strip()] for i in range(dim[0])]
    next_move(pos[0], pos[1], dim[0], dim[1], board)