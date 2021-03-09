'''
THis code print fine for book library
1. if returned in next year fine => 10000
2. if returned in next month => months * 500
3. if returned in next days => days * 15
'''


ret_d, ret_m, ret_y = map(int, input().split())
ex_d, ex_m, ex_y = map(int, input().split())

if (ex_y < ret_y):
    print('10000')
elif (ret_m > ex_m) and (ex_y == ret_y):
    print((ret_m - ex_m) * 500)
elif (ret_d > ex_d) and (ret_m == ex_m) and (ex_y == ret_y):
    print((ret_d - ex_d) * 15)
else:
    print('0')