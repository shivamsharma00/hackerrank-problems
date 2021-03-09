'''
We have a cleaning bot which needs to clean the area in most optimized way.

INPUT               OUTPUT

b---d               RIGHT
-d--d
--dd-
--d--
----d



-b--d               DOWN
-d--d
--dd-
--d--
----d
'''

up = 'UP'
down = 'DOWN'
left = 'LEFT'
right = 'RIGHT'


# function to find most less way
def next_move(posr, posc, board):
    size = 5
    c_diff = 1000
    r_diff = 1000

    bots = [[i, j] for i in range(size)
                   for j in range(size)
                   if board[i][j]=='d']
    


    r_bot = [bots[i] for i in range(len(bots))
                   if bots[i][0]==posr]

    c_bot = [bots[i] for i in range(len(bots))
                     if bots[i][1]==posc]
   
    print("r_bot is : {}".format(r_bot))
    print('c_bot is : {}'.format(c_bot))
    if r_bot:
        c_diff = abs(r_bot[0][1] - posc)
    if c_bot:
        r_diff = abs(c_bot[0][0] - posr)

    print('c_diff is : {}'.format(c_diff))
    print('r_diff is : {}'.format(r_diff))
    if c_diff > r_diff:
        # bot will move in column
        if posr > r_bot[0][1]:
            print(up)
        else:
            print(down)
    elif r_diff > c_diff:
        # bot will move in row
        if posc > r_bot[0][0]:
            print(left)
        else:
            print(right)

    

'''
Hackerrank's short hand code

def next_move(posr, posc, board):
    i, j = min(((i, j) for i, row in enumerate(board) if 'd' in row for j, c in enumerate(row) if c == 'd'), key=lambda x: abs(posr - x[0]) + abs(posc - x[1]))
    print("LEFT" if j < posc else "RIGHT" if j > posc else "UP" if i < posr else "DOWN" if i > posr else "CLEAN")
'''


# Driver code
if __name__ == "__main__":
    # pos = [int(i) for i in input().strip().split()]
    # board = [[j for j in input().strip()] for i in range(5)]
    pos = [0, 1]
    board = [['-', 'd', '-', '-', '-'],
             ['-', 'd', '-', '-', '-'],
             ['-', '-', '-', 'd', '-'],
             ['-', '-', '-', 'd', '-'],
             ['-', 'b', 'd', '-', 'd']]
    next_move(pos[0], pos[1], board)