import sys

s = input().strip()

try:
    line = int(s)
except ValueError:
    print("Bad String")
else:
    print(line)