def stones(n, a, b):
    a1 = []
    a2 = []
    for i in range(0, n):
        res = ((n-1)-i)*a+(i*b)
        if (res in a1):
            pass
        else:
            a1.append(res)
    return a1



if __name__ == '__main__':
    n = [58, 83, 73, 12, 5]
    a = [69, 86, 25, 73, 3]
    b = [24, 81, 25, 82, 23]

    # for i in range(0, len(n)):
    #     res = stones(n[i], a[i], b[i])
    #     print(str(i)+"- "+str(res))
    res = stones(83, 86, 81)
    print(res)