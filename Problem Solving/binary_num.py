a = 439
b = []

while a>0:
    b.append(a%2)
    a = int(a/2)
b.reverse()
print(b)

n_count = 0
count = 0
max_arr = []
while count<len(b):
    if b[count] == 1:
        n_count+=1
        if count == len(b)-1:
            max_arr.append(n_count)
    else:
        if n_count != 0:
            max_arr.append(n_count)
            n_count = 0
    count+=1

print(max(max_arr))
