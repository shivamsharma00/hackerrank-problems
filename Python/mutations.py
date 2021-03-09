'''
lists - mutable
tuples - immutaple

To make changes to tuples
1. Convert string into a list and than change the value.
>>> string = "abracadabra"
>>> l = list(string)
>>> l[5] = 'k'
>>> string = ''.join(l)
>>> print string
abrackdabra 

2. Slice the string and join it back.
>>> string = string[:5] + "k" + string[6:]
>>> print string
abrackdabra
'''
