#

def nextMove(n,r,c,grid):
    princess_pos = []
    for row in range(n):
        try:
            princess_pos = [row, grid[row].index('p')]
        except ValueError :
            pass
    if r == princess_pos[0]:
        if c == princess_pos[1]:
            pass
        step = "RIGHT" if c < princess_pos[1] else "LEFT"
    elif r < princess_pos[0]:
        step = "DOWN"
    else:
        step = "UP"     
    return step

n = int(input())
r,c = [int(i) for i in input().strip().split()]
grid = []
for i in range(0, n):
    grid.append(input())

print(nextMove(n,r,c,grid))