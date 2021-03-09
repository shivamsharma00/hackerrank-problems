'''
an integer N, integers r and c indicating the row & column position of the bot
and the character array grid - and outputs the next move the bot makes to rescue the princess.
Sample Input

5
2 3
-----
-----
p--m-
-----
-----

Sample Output
LEFT
'''

def nextMove(n, b_r, b_c, grid):
    up = 'UP'
    down = 'DOWN'
    left = 'LEFT'
    right = 'RIGHT'

    p_pos = [[i, j] for i in range(n)
                    for j in range(n)
                    if grid[i][j]=='p']
    p_r = p_pos[0][0]
    p_c = p_pos[0][1]
    
    if (p_r>b_r):
        return down
    elif(b_r>p_r):
        return up
    else:
        pass
    
    if (p_c>b_c):
        return right
    elif(b_c>p_c):
        return left
    else:
        pass
    
    
n = 5
r = 2
c = 3

grid = [['-', '-', '-', '-', '-'], ['-', '-', '-', '-', '-'], ['p', '-', 'm', '-', '-'], ['-', '-', '-', '-', '-'], ['-', '-', '-', '-', '-']]
print(nextMove(n, r, c, grid))