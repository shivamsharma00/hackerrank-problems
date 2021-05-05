'''
This is Python problem from HackerRank by name "Nested List".
We have sorted dictionary by values.
THis code prints all the second lowest values.
'''

# this is short hand code
marksheet = [[input(), float(input())] for _ in range(int(input()))]
sh = sorted(list(set([marks for name , marks in marksheet])))[1]
print('\n'.join([a for a, b in sorted(marksheet) if b == sh]))

''''
if __name__ == '__main__':
    mark = dict()
    for _ in range(int(input())):
        l_name = input()
        score = float(input())
        mark[l_name] = score

    
    # reverse will sort in descending order
    new_dic = {k:v for k, v in sorted(mark.items(), key = lambda x : x[-1], reverse=True)}
    dic_val = list(new_dic.values())
    dic_keys = list(new_dic.keys())

    max_n = len(new_dic) - 1
    # lar_val = next(v for i, v in enumerate(new_dic.iter))
    lar_val = dic_val[max_n]
    max_n -=1
    sec_lar_value = dic_val[max_n]
    while lar_val == sec_lar_value:
        max_n -=1
        lar_val = sec_lar_value
        sec_lar_value = dic_val[max_n]
    
    while dic_val[max_n] == sec_lar_value:
        print(dic_keys[max_n])
        max_n-=1
'''    
    