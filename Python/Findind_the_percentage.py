'''
This file contain code of finding percentage of the given person from a dictionary.
'''

if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    

    # {:.2f} is used for two decimal places in python
    index = 0
    while  list(student_marks.keys())[index] != query_name:
        index+=1
    print("{:.2f}".format(sum(list(student_marks.values())[index])/3))
    

    '''
    short hand implementation
    
    print("{:.2f}".format(sum(list(student_marks[query_name]))/3))
    '''