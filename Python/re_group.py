
### For more information    https://docs.python.org/3/library/re.html

'''

group()
- A group() expression returns one-or-more subgroups of the match.

m = re.match(r'(\w+)@(\w+)\.(\w+)','username@hackerrank.com')
m.group(0)       # The entire match 
'username@hackerrank.com'
m.group(1)       # The first parenthesized subgroup.
'username'
m.group(2)       # The second parenthesized subgroup.
'hackerrank'
m.group(3)       # The third parenthesized subgroup.
'com'
m.group(1,2,3)   # Multiple arguments give us a tuple.
('username', 'hackerrank', 'com')
-----------------------------------------------------------------


groups()
- A groups() expression returns a tuple containing all the subgroups of the match.

m = re.match(r'(\w+)@(\w+)\.(\w+)','username@hackerrank.com')
m.groups()
('username', 'hackerrank', 'com')
-----------------------------------------------------------------


groupdict()
- A groupdict() expression returns a dictionary containing all the named subgroups of the match, keyed by the subgroup name.


m = re.match(r'(?P<user>\w+)@(?P<website>\w+)\.(?P<extension>\w+)','myname@hackerrank.com')
m.groupdict()
{'website': 'hackerrank', 'user': 'myname', 'extension': 'com'}

'''


import re

string = '..12345678910111213141516171820212223'
m = re.match(r'(\[0-9])\1*', string)
if m:
    print("found: {}".format(m.group(0)))
else:
    print("Not found")



import re
m = re.search(r'([a-zA-Z0-9])\1+', input().strip())
print(m.group(1) if m else -1)