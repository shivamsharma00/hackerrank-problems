arr = [4, 4, 3, 4]

count = 0
for j in range(len(arr)):
    for i in range(j, len(arr)):
        if arr[j] > arr[i]:
            count += 1

print(arr)
print(count)