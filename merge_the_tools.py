s = 'AAABCADDE'
k = 3

var = 0
for i in range(int(len(s)/k)):
    l1 =''
    # print(i)
    temp_s = s[var:(k*i+k)]
    var = (k*i + k)
    for a in temp_s:
        if a not in l1:
            l1 = l1 + a
        else:
            pass

    print(l1)