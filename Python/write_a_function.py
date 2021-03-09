'''
In the Gregorian calendar, three conditions are used to identify leap years:

    The year can be evenly divided by 4, is a leap year, unless:
        The year can be evenly divided by 100, it is NOT a leap year, unless:
            The year is also evenly divisible by 400. Then it is a leap year.
'''

def is_leap(year):
    '''
    Actual code for the problem
    leap = False
    if year%4 ==0:
        if year%100 ==0:
            if year%400==0:
                leap = True
            else:
                leap = False
        else:
            leap = True
    return leap
    '''
    # Short hand code for above problem
    return ((True if year%400==0 else False) if (year%100==0) else True) if year%4==0 else False


if __name__=='__main__':
    yr = int(input())
    print(is_leap(yr))
