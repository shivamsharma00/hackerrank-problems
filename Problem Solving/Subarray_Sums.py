
def findsum(numbers, queries):
    query_row = len(queries)
    sum = 0


    for i in range(query_row):
        sum = 0
        for j in range(queries[i][0], queries[i][1]+1, 1):
            index = j - 1
            if (numbers[index]==0):
                sum = sum + queries[i][2]
            sum = sum + numbers[index]
        print(sum)    
           
n = [-5, 0]
q = [[2, 2, 20]]
findsum(n, q)