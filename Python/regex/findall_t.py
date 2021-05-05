
### For more information    https://docs.python.org/3/library/re.html


'''

findall() is probably the single most powerful function in the re module.
Above we used re.search() to find the first match for a pattern. findall() 
finds *all* the matches and returns them as a list of strings, with each string representing one match.

'''
import re

## suppose we have a text with many email addresses
str = 'purple alice@google.com, blah monkey bob@abc.com blah dishwasher'

## Here re.findall() returns a list of all the found email strings
emails = re.findall(r'[\w\.-]+@[\w\.-]+', str)  ## alice@google.com     bob@abc.com
if emails:
    print(emails)
else:
    print("NOt found")
    