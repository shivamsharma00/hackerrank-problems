def almost_sorted(a):
    x = 0
    y = len(a)-1
    
    while a[x]<=a[x+1]:
        x+=1
    while a[y]>=a[y-1]:
        y-=1

    b = a[x:y+1]
    b[0], b[-1] = b[-1], b[0]

    cond_l = True if x-1<0 else b[0]>=a[x-1]
    cond_r = True if y+1==len(a) else b[-1]<=a[y+1] 

    if cond_l and cond_r:
        for i in range(len(b)-1):
            if b[i]>b[i+1]:
                break
        else:
            return "yes\nswap %s %s"%(x+1, y+1)
    
    b[0], b[-1] = b[-1], b[0]

    cond_l = True if x-1<0 else a[x-1]<=b[-1]
    cond_r = True if y+1==len(a) else a[y+1]>=b[0]

    if cond_l and cond_r:
        for i in range(len(b)-1):
            if b[i]<b[i+1]:
                break
        else:
            return "yes\nreverse %s %s" %(x+1, y+1)
        
    return 'no'
    
if __name__ == '__main__':
    a = [1, 5, 4, 3, 2, 6]
    print(almost_sorted(a))