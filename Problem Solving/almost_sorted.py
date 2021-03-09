def sort_or_not(arr):
    # print("sort1")
    # arr1 = arr[:]
    # arr.sort()
    # if (arr1 == arr):
    #     return 1
    # else:
    #     return 0
    flag = 0
    for i in range(1, (len(arr))):
        if (int(arr[i]) > int(arr[i-1])):
            # print(arr[i])
            # print(arr[i-1])
            pass
        else:
            flag += 1

    # print(flag)
    if flag == 0:
        return 1
    else:
        return 0


if __name__ == '__main__':
    f = open("sort_data.txt", "r")
    for line in f:
        a = line.split(" ")
    # a = [3, 1, 2]
    # temp1 = a[11]
    # a[11] = a[94]
    # a[94] = temp1
    # print(a[11])
    # print(a[94])
    
    # a1 = a[:]
    swap_flag = 0
    rev_flag = 0
    
    # print(a[94])

    if (sort_or_not(a)==1):
        print("yes")
    else:
        # print(a)
        for i in range(0, len(a)):
            for j in range(i+1, len(a)):
                # print("here")
                a2 = a[:]
                temp = a2[i]
                a2[i] = a2[j]
                a2[j] = temp
                # print("a2- "+str(a2))
                if (sort_or_not(a2)==1):
                    swap_flag = 1
                    print("yes")
                    print("swap "+str(i+1)+" "+str(j+1))
                    break
                    break
                else:
                    if swap_flag != 1:
                    # print("in else")
                        swap_flag = 0

        if (swap_flag == 0):
            print("in 1")
            for i in range(1, len(a)):
                for j in range(i+3, len(a)):
                    a3 = a[:]
                    a4 = a3[i:j]
                    a5 = a4[:]
                    a5.reverse()
                    # print("a5- "+str(a5))
                    if (sort_or_not(a5)==1):
                        new_arr = a[0:i] + a5 + a[j:len(a)]
                        new_arr_sub = new_arr[:]
                        if (sort_or_not(new_arr_sub)==1):
                            print("yes")
                            print("reverse "+str(i+1)+" "+str(j))
                            rev_flag = 1
                            # print("new Array - "+str(new_arr))
                        # pass
                    
                    # print(str(i)+" - "+str(j))
            if rev_flag == 0:
                print("no")
        # else:
            # print("no")












# *****************************************************************************
# SOLUTIONS


def almostSorted(a):
    x = 0
    y = len(a)-1
    while a[x]<=a[x+1]:
        x+=1
    while a[y]>=a[y-1]:
        y-=1

    b = a[x:y+1]
    b[0],b[-1]=b[-1],b[0]

    cond_l = True if x-1<0 else b[0]>=a[x-1]
    cond_r = True if y+1==len(a) else a[y+1]>=b[-1]
    if cond_l and cond_r:
        for i in range(len(b)-1):
            if b[i]>b[i+1]:
                break
        else:
            return "yes\nswap %s %s"%(x+1,y+1)
        
    b[0],b[-1]=b[-1],b[0]
    
    cond_l = True if x-1<0 else a[x-1]<=b[-1]
    cond_r = True if y+1==len(a) else  b[0]<=a[y+1]
    if cond_l and cond_r:
        for i in range(len(b)-1):
            if b[i]<b[i+1]:
                break
        else:
            return "yes\nreverse %s %s"%(x+1,y+1)
    return "no"


n = int(input())
arr = list(map(int, input().split()))
print(almostSorted(arr))


                
