import math

def stoneDivision(n, s):
    step_count = 0
    l = len(s)
    a = s

    for i in range(l):
        sorter = 0
        for j in range(l-1):
            if a[j]>a[j+1]:
                temp = a[j+1]
                a[j+1] = a[j]
                a[j] = temp
                sorter+=1
        if sorter==0:
            break
    
    current_divisor = n
    no_of_set = 0
    flag = 0

    for i in range((l-1), -1, -1):
        print('Current Divisor-{} step count-{} no of set-{}'.format(current_divisor,step_count,no_of_set))
        if a[i]<n:
            if current_divisor%a[i]==0:
                current_divisor=a[i]
                step_count+=no_of_set
                no_of_set=(n/a[i])
                flag=1
            # step_count+=1
        
    print('Current Divisor-{} step count-{} no of set-{}'.format(current_divisor,step_count,no_of_set))

    # print("array is sorted")
    if flag:
        print(step_count+1)
    else:
        print(step_count)





if __name__ == '__main__':
    n = 377083280820
    S = [1, 377083280820, 2, 188541640410, 3, 125694426940, 4, 94270820205, 5, 75416656164]
    stoneDivision(n, S)
    