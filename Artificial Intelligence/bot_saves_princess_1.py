'''
Sample Input

3
---
-m-
p--

Sample Output
DOWN
LEFT
'''


def displayPathtoPrincess(n,grid):

    up = 'UP'
    down = 'DOWN'
    right = 'RIGHT'
    left = 'LEFT'

    princess_pos = [[i,j] for i in [0, n-1]
                          for j in [0, n-1]
                          if grid[i][j]=='p']
    bot_pos = [[i,j] for i in range(n)
                     for j in range(n)
                     if grid[i][j]=='m']

    vertical_diff = abs(princess_pos[0][0]-bot_pos[0][0])
    hori_diff = abs(princess_pos[0][1]-bot_pos[0][1])

    if (princess_pos[0][0]>bot_pos[0][0]):
        for i in range(vertical_diff):
            print(down)
    elif(bot_pos[0][0]>princess_pos[0][0]):
        for i in range(hori_diff):
            print(up)
    else:
        pass

    if (princess_pos[0][1]>bot_pos[0][1]):
        for i in range(vertical_diff):
            print(right)
    elif(bot_pos[0][1]>princess_pos[0][1]):
        for i in range(hori_diff):
            print(left)
    else:
        pass
    
    print(bot_pos)
    print(princess_pos)                          
#print all the moves here

# m = int(input())
m = 3
grid = [['-', '-', '-'], ['-', 'm', '-'], ['p', '-', '-']] 
# for i in range(0, m): 
#     grid.append(input().strip())

displayPathtoPrincess(m,grid)