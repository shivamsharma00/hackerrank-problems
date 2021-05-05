'''
THis file contains HAckerrank code for problem of list.
'''

N = int(input())
l = []

for i in range(N):
    c = input().split()

    l.insert(int(c[1]), int(c[2])) if c[0] == 'insert' else print(l) if c[0] == 'print' else l.remove(int(c[1])) if c[0] == 'remove' else \
    l.append(int(c[1])) if c[0] == 'append' else l.sort() if c[0] == 'sort' else l.pop() if c[0] == 'pop' else l.reverse()

'''
    if command[0] == 'insert':
        l.insert(command[1], command[2])
    elif command[0] == 'print':
        print(l)
    elif command[0] == 'remove':
        l.remove(command[1])
    elif command[0] == 'append':
        l.append(command[1])
    elif command[0] == 'sort':
        l.sort()
    elif command[0] == 'pop':
        l.pop()
    elif command[0] == 'reverse':
        l.reverse()
    else:
        print("wrong command")
'''
