'''
Suppose you want to find the email address inside the string 'xyz alice-b@google.com purple monkey'.\
We'll use this as a running example to demonstrate more regular expression features.
Here's an attempt using the pattern r'\w+@\w+':
'''
import re

str = 'purple alice-b@google.com monkey dishwasher'
match = re.search('\w+@\w+', str)
# it will give "b@google" because it can't idetify '-' and '.' 


'''
Square Brackets

Square brackets can be used to indicate a set of chars, so [abc] matches 'a' or 'b' or 'c'. 
The codes \w, \s etc. work inside square brackets too with the one exception that dot (.)
just means a literal dot. For the emails problem, the square brackets are an easy way 
to add '.' and '-' to the set of chars which can appear around the @ with the pattern r'[\w.-]+@[\w.-]+' 
to get the whole email address:
'''
match = re.search(r'[\w.-]+@[\w.-]+', str)      
if match:
    print (match.group())  ## 'alice-b@google.com'




### For more information    https://docs.python.org/3/library/re.html

'''
Group Extraction
The "group" feature of a regular expression allows you to pick out parts of the matching text.
Suppose for the emails problem that we want to extract the username and host separately. 
To do this, add parenthesis ( ) around the username and host in the pattern, 
like this: r'([\w.-]+)@([\w.-]+)'. In this case, the parenthesis do not change what the pattern will match, 
instead they establish logical "groups" inside of the match text. On a successful search, 
match.group(1) is the match text corresponding to the 1st left parenthesis,
and match.group(2) is the text corresponding to the 2nd left parenthesis. 
The plain match.group() is still the whole match text as usual.
'''

str = 'purple alice-b@google.com monkey dishwasher'
match = re.search(r'([\w.-]+)@([\w.-]+)', str)
if match:
    print(match.group())
    print(match.group(1))
    print(match.group(2))
else:
    print("Not Found")