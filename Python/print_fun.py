'''
n = int(input())
for i in range(1, n+1):
    print(i, sep='')
'''

# short hand code
print(*range(1, int(input())+1), sep='')