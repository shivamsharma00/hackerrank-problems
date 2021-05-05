# This script contians code for the text alignment in python.

w = 20
# Below code will left align the 'HackerRank' and fill the remaining width by '-'
print('HackerRank'.ljust(w, '-'))
# Below code will center align the 'HackerRank' and fill the remaining width by '-'
print('HackerRank'.center(w, '-'))
# Below code will right align the 'HackerRank' and fill the remaining width by '-'
print('HackerRank'.rjust(w, '-'))




thickness = int(input()) #This must be an odd number
c = 'H'

#Top Cone
for i in range(thickness):
    print((c*i).rjust(thickness-1)+c+(c*i).ljust(thickness-1))

#Top Pillars
for i in range(thickness+1):
    print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))

#Middle Belt
for i in range((thickness+1)//2):
    print((c*thickness*5).center(thickness*6))    

#Bottom Pillars
for i in range(thickness+1):
    print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))    

#Bottom Cone
for i in range(thickness):
    print(((c*(thickness-i-1)).rjust(thickness)+c+(c*(thickness-i-1)).ljust(thickness)).rjust(thickness*6))