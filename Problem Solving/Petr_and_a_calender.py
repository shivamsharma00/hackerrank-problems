# Written By : Shivam Sharma
# This code takes two inputs (month number and weekday number) 
# and prints how many weeks will be
# there in that month or the week columns.
def main():
    month = {"1":"31", "2":"30", "3":"31", "4":"30", "5":"31","6":"30", 
             "7":"31", "8":"31", "9":"30", "10":"31", "11":"30", "12":"31"}
    column = 1

    m = input("Enter Month: ")
    d = int(input("Enter Day: "))
    
    days_in_month = (int(month[m]) - (8-d))
    column = column + int(days_in_month/7) + 1

    print("Column: "+str(column))

main()
