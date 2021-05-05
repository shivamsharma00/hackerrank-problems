'''
The re.sub() tool (sub stands for substitution) evaluates a pattern and, for each valid match, it calls a method (or lambda).
The method is called for all matches and can be used to modify strings in different ways.
The re.sub() method returns the modified string as an output.
'''
import re

lines = ""
N = int(input())
for _ in range(N):
    lines+=input()+'\n'

# new_lines = re.sub(" && ", " and ", lines)
lines_2 = re.sub(" || ", " or ", lines)

print(lines_2)


for i in range(N):
    print(re.sub(r'(?<= )(&&|\|\|)(?= )', lambda x: 'and' if x.group() == '&&' else 'or', input() ))


'''
a = 1;
b = input();
if a + b > 0 && a - b < 0:
    start()
elif a*b > 10 || a/b < 1:
    stop()
'''