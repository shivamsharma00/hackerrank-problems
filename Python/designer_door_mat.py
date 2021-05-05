
def mat(l):
    N = l
    M = l*3
    s1 = ''
    s2 = ''
    s3 = ''
    m = 1

    for i in range(l//2):
        # print(i)
        temp = ''
        num = int((M-((i+m)*3))/2)
        temp += num*'-' + '.|'
        for j in range((i+m)-1):
            temp += '..|'
        temp= temp + '.' + num*'-' + '\n'

        # if i == ((l//2)-1):
        #     pass
        # else:
        #     temp += '\n'
            # print('in here,', (l//2-1), i)

        m +=1
        s3 = temp+s3
        s1 += temp
    s2 = int((M - len('WELCOME'))/2)*'-' + 'WELCOME' + int((M - len('WELCOME'))/2)*'-' + '\n'
    return s1+s2+s3


print(mat(29))