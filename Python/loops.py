'''
print square of all numbers less than n.
'''
n = int(input())
# make a list of name res with squared elements in it.
res = [i*i for i in range(n)]
# to print the list elements in separate line
print(*res, sep="\n")