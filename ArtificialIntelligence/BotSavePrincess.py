#!/usr/bin/python

def displayPathtoPrincess(n,grid):
    #print all the moves here
    bot_pos = []
    princess_pos = []
    for row in range(n):
        for col in range(n):
            if grid[row][col] == 'm':
                bot_pos = [row,col]
            if grid[row][col] == 'p':
                princess_pos = [row,col]
    steps = []
    if bot_pos[0]==princess_pos[0] and bot_pos[1]==princess_pos[1]:
        return None
    elif bot_pos[0] < princess_pos[0]:
        steps.extend(["DOWN" for step in range(bot_pos[0],princess_pos[0])])
    else:
        steps.extend(["UP" for step in range(princess_pos[0],bot_pos[0])])
    if bot_pos[1] < princess_pos[1]:
        steps.extend(["RIGHT" for step in range(bot_pos[1],princess_pos[1])])
    else:
        steps.extend(["LEFT" for step in range(princess_pos[1],bot_pos[1])])
    print("\n".join(steps))
    
        
    

m = int(input())
grid = [] 
for i in range(0, m): 
    grid.append(input().strip())

displayPathtoPrincess(m,grid)