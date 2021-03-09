from os import supports_dir_fd


a = '06:40:03AM'
count = 0
hr =  ""
min = ""
sec = ""
for i in range(0, len(a)):
    
    if a[i] == ":":
        count +=1
        
    else:
        if count == 0:
            hr = hr + a[i]
        elif count == 1:
            min = min+a[i]
        elif count == 2:
            sec = sec+str(a[i])
print(hr)
dul = sec[-2:]
sec = sec[:2]
if dul == "AM":
    if (hr == '12'):
        print(hr)
        hr = "00"
    else:
        pass
else:
    if (int(hr) == 12):
        hr = str(hr)
    else:
        hr = str(int(hr)+12)
print(hr)

time1 = str(hr)+":"+min+":"+sec
print(time1)