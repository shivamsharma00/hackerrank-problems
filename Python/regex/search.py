

### For more information    https://docs.python.org/3/library/re.html

'''
This is the sample code to understand searching in regular expressions.
'''

import re

testStringL = "Time to say Hello World"
# One method to search
match_object = re.search(r"(H....)", testStringL)
print (match_object.group())


# alternative method to search
pattern = "Hello"
match = re.search(pattern, testStringL)
# do condition check after search 
if match:
    print("Found : {}".format(match.group()))
else:
    print("Not Found !!!")


# Recommended approach to use re.search()
str = 'an example word:cat!!'
# The 'r' at the start of the pattern string designates a python "raw"
# string which passes through backslashes without change which is very handy for regular expressions 
match = re.search(r'word:\w\w\w', str)
# If-statement after search() tests if it suceeded
if match:
    print('Found: {}'.format(match.group()))
else:
    print('Not Found !!!')


match = re.search(r'iii', 'piiing')     # found, match.group() == 'iii'
match = re.search(r'..g', 'piiing')     # found, match.group() == 'ing'
## \d = digit char,     \w = word char
match = re.search(r'\d\d\d', 'p123g')   # found, match.group == "123"
match = re.search(r'\w\w\w', '123abcdsa@@')     # found, match.group() == 'abc'


## Repetition Examples

### i+ = one or more i's, as many as possible.
match = re.search(r'pi+', 'piiiiing')   # found, match.group() == ''piiiii'

### finds the first/leftmost solution, and within it drives the +
### as far as possible (aka 'leftmost and largest')
### In this example, note that it does not get to the second i's
match = re.search(r'i+', 'piiiniiiiig')     # found, match.group() == 'iii'

### \s* = zero or more whitespace chars
### Here look for 3 digits seprated by whutespace
match = re.search(r'\d\s*\d\s*\d', 'xx1 2      3xx')    # found, match.group() == '1 2    3'
match = re.search(r'\d\s*\d\s*\d', 'xx123xx')           # found, match.group() == '123'

### ^ = matches the start of a string, so this fails:
match = re.search(r'^b\w+', 'foobar')       # Not found
### but without ^, it succeeds:
match = re.search(r'b\w+', 'foobar')        # found, match.group() == 'bar'



if match:
    print('Found: {}'.format(match.group()))
else:
    print('Not Found !!!')


'''
 a, X, 9, < -- ordinary characters just match themselves exactly.
 The meta-characters which do not match themselves because they
 have special meanings are: . ^ $ * + ? { [ ] \ | ( ) 

 -> . (a period) -- matches any single character except newline '\n'

 -> \w -- (lowercase w) matches a "word" character: a letter or digit or underbar [a-zA-Z0-9_].
          Note that although "word" is the mnemonic for this, it only matches a single word char,
          not a whole word. \W (upper case W) matches any non-word character.

 -> \b -- boundary between word and non-word

 -> \s -- (lowercase s) matches a single whitespace character -- space, newline,
          return, tab, form [ \n\r\t\f]. \S (upper case S) matches any non-whitespace character.

 -> \t, \n, \r -- tab, newline, return

 -> \d -- decimal digit [0-9] (some older regex utilities do not support but \d, but they all support \w and \s)

 -> ^ = start, $ = end -- match the start or end of the string

 -> \ -- inhibit the "specialness" of a character. So, for example, use \. to match a 
         period or \\ to match a slash. If you are unsure if a character has special meaning, 
         such as '@', you can put a slash in front of it, \@, to make sure it is treated just as a character.
'''