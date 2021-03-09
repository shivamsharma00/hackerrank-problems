''''
Output the integer number indicating the total number of occurrences of the substring in the original string.

ABCDCDC
CDC

2
'''
def count_substring(string, sub_string):
    '''
Bigger version of code 
    '''    

    # sub_len = len(sub_string)
    # s_len = len(string)
    # count = 0
    # for i in range(s_len-sub_len+1):
    #     if string[i:i+sub_len]==sub_string:
    #         count+=1
    # return count
    '''
Shrt hand version of code 
    '''    
    
    return (sum([1 for i in range(len(string)-len(sub_string)+1) if string[i:i+len(sub_string)]==sub_string]))


if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)