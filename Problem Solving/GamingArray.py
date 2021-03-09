arr_len = int(input())
a = []
for i in range(arr_len):
    c = int(input())
    a.append(c)
print(a)
s = a
count = 0
while (len(s)!=0):
    max_n = 0
    p_count = 0
    t_place = 0

    max_n = max(s)
    t_place = s.index(max_n)
    # a = [i for i in s if ]
    # for num in s:
    #     p_count = p_count + 1
    #     if num > max_n:
    #         max_n = num
            # t_place = p_count
    s = s[: (t_place)]
    count = count + 1
    # print("Count-"+str(count))
    # print("new string - "+str(s))

print(count)
if (count%2==0):
    print("ANDY")
else:
    print("BOB")

    

