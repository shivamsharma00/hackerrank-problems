'''
Read an integer n,
* If n is odd, print Weird
* If n is even and in the inclusive range of 2 to 5, print Not Weird
* If n is even and in the inclusive range of 6 to 20, print Weird
* If n is even and greater than 20, print Not Weird
'''
n = int(input().strip())
'''
This style of writing if-else loop is called short-hand code.
This style works when only one instruction to be executed in if condition.
'''
print("Weird") if (n%2!=0) else (print("Weird") if (6<=n<=20) else print("Not Weird"))