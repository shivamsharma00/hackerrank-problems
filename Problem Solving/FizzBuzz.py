
num = int(input("Enter the number :"))

for i in range(num):
    ele = i + 1
    if (ele % 3 ==0):
        if (ele%5==0):
            print("FizzBuzz")
        else:
            print("Fizz")
    elif (ele%5 == 0):
        print("Buzz")
    else:
        print(ele)
