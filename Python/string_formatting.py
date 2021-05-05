def int_to_binary(n):
    s = ''
    while n > 1:
        s = str(n%2) + s
        n = n//2
    s = "1" + s
    return s

def int_to_octal(n):
    s = ''
    while n > 7:
        s = str(n%8) + s
        n = n//8
    s = str(n) + s
    return s

def int_to_hexa(n):
    s = ''
    hexa = {10:'A', 11:'B', 12:'C', 13:'D', 14:'E', 15:'F'}
    while n > 15:
        print("here")
        temp = n % 16
        if temp in hexa.keys():
            temp = hexa[temp]
        s = str(temp)+s
        # s = str(n%16)+ s
        n = n // 16
    
    s = str(n) + s
    return s



def print_formatted(number):
    s = ''
    dis = len(int_to_binary(number))
    for i in range(1, number+1, 1):
        s = s + str(i).rjust(len(str(number))) + int_to_octal(i).rjust(dis+1) + int_to_binary(i).rjust(dis+1) + '\n'
        # if i>7:
            # if i
            # s += str(i+2).rjust(dis+1)
        # s += '\n'

    return s
        


# print(int_to_binary(17))
# print(print_formatted(17))
# print(int_to_hexa(17))
# print(int_to_octal(1))




n = int(input())
width = len("{0:b}".format(n))
for i in range(1, n+1, 1):
    print('{0:{width}d} {0:{width}o} {0:{width}X} {0:{width}b}'.format(i, width=width))