def print_rangoli(size):

    a = 'abcdefghijklmnopqrstuvwxyz'

    n = size
    s1 = ''
    s2 = ''
    s3 = ''
    s = ''
    for i in range(n-1):
        # print('in here')
        s1 = ''
        if i == 0:
            s1 = s1 + '-' * (((n-1)*2)-(2*i)) + '-'.join(a[n-1:((n-1)-(i+1)):-1])+ '-'.join(a   [((n-1)-(i-1)):n]) +  '-' * (((n-1)*2)-(2*i)) + '\n'
        else:
            s1 = s1 + '-' * (((n-1)*2)-(2*i)) + '-'.join(a[n-1:((n-1)-(i+1)):-1])+ '-' +    '-'.join(a[((n-1)-(i-1)):n]) +  '-' * (((n-1)*2)-(2*i)) + '\n'
            
        s += s1
        
        if i == 0:
            s1 = ''
            s1 = s1 + '-' * (((n-1)*2)-(2*i)) + '-'.join(a[n-1:((n-1)-(i+1)):-1]) +    '-'.join(a[((n-1)-(i-1)):n]) +  '-' * (((n-1)*2)-(2*i))
            s3 = s1 + s3
        else:
            s3 = s1 + s3
    # print('-'.join(a[(n-1)::-1]))
    if n != 1:
        s2 = '-'.join(a[(n-1)::-1])+ '-' + '-'.join(a[1:n]) + '\n'
    else:
        s2 = a[n-1]
    print(s+s2+s3)
if __name__ == '__main__':
    n = int(input('Enter number: '))
    print_rangoli(n)