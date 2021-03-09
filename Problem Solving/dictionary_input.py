import sys

f = open("data.txt", "r")
number = int(f.readline())
dict = {}
count_p = 0
count_n = 0

# phone_book = dict(input().split() for _ in range(n))

# while count_p<number:
numbers = [f.readline().split(" ") for _ in range(number)]

    dict[a] = b
    count_p += 1
number_1 = 5
# while count_n<number_1:
#     new = f.readline()[0:-1]
new = [f.readline().split() for i in range(0, )]
# print(newlist)
# print(new[0])
new1 = new[1]
new1 = new1[0:-1]
# new[0] = new[0][0:-1]
a = (str(new1)+"="+str(dict[new1])) if (new1 in dict.keys) else ("Not found")
print(a)
    # if (new in dict):
    #     print(str(new)+"="+str(dict[new]))
    # else:
    #     print("Not found")
    #     # sys.stdout.write("Not")
    # count_n+=1




n = int(input())
name_numbers = [input().split() for _ in range(n)]
phone_book = {k: v for k,v in name_numbers}
while True:
    try:
        name = input()
        if name in phone_book:
            print('%s=%s' % (name, phone_book[name]))
        else:
            print('Not found')
    except:
        break