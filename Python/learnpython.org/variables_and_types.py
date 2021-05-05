mystring = 'hello'
myfloat = 10.0
myint = 20

if mystring == 'hello':
    print("string: %s" %mystring)
if isinstance(myfloat, float) and myfloat == 10.0:
    print('Float : %f' %myfloat)
if isinstance(myint, int) and myint == 20:
    print('integer : %d' %myint)


name = "John"
age = 20
# we use tuple to print multiple variables
print('Name is %s and age is %d' %(name, age))


arr = [1, 2, 3]
# %s can be used other than string variables
print('lsit is %s' %arr)

'''
%s - String (or any object with a string representation, like numbers)
%d - Integers
%f - Floating point numbers
%.<number of digits>f - Floating point numbers with a fixed amount of digits to the right of the dot.
%x/%X - Integers in hex representation (lowercase/uppercase)
'''

astr = "Hello World"
print(len(astr))
print(astr.index('o'))
print(astr.count('l'))
print(astr[3:7])       # print slice [start:stop:step]
print(astr[3:7:1])
print(astr[::-1])   # reverse string
print(astr.upper())
print(astr.lower())
print(astr.startswith('Hello'))     # retrun True
print(astr.endswith('asdasd'))      # return False
new_str = astr.split(" ")           # split at space
print(new_str)



x = 2
y = 1
ar = [1, 2 ,3]
print(x==2)     # print true
print(x==3)     # print False
print(x < 3)    # print true
print(x is 2)   # print true
print(y in ar)  # print true
print(not False)    # print True
print((not False) == (False))   # print False


'''
break is used to exit a for loop or a while loop, whereas continue is
used to skip the current block, and return to the "for" or "while" statement. 
'''
count = 0
while True:
    print(count)
    count+=1
    if count >= 5:
        break

# only print odd numbers
for x in range(10):
    if x % 2 == 0:
        continue
    print(x)


'''
Unlike languages like C,CPP.. we can use else for loops.
When the loop condition of "for" or "while" statement fails then 
code part in "else" is executed. If a break statement is executed
inside the for loop then the "else" part is skipped. Note that the "else"
part is executed even if there is a continue statement.
'''
count = 0
while(count < 5):
    print(count)
    count+=1
else:
    print('count value have reached %s' %(count))


for i in range(1, 10):
    if (i % 5 == 0):
        break
    print(i)
else:
    print("THis will not be printed!!")

