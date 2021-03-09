if __name__ == '__main__':
    mark = {}
    for _ in range(int(input())):
        l_name = input()
        score = float(input())
        mark.update(name=score)
        # mark[name] = score
    
    mark = sorted(mark)    
    print(mark)
    key_list = mark.keys()
    n = []
    runner_up = 1000
    for items in mark.values:
        if (items>min(mark.values))&(items<=runner_up):
            runner_up = items
            pos = mark.index(items)
            print(key_list[pos])
    
        
    
    