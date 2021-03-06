'''
Identifiers:
\d any number
\D anything but a number

\s space
\S anything but a space

\w any caharcter
\W anything but a character

. any character except for a newline

\b the whitespace around words

\. a period

Modifiers:
{x,y} expecting x to y of something
+ match 1 or more
? match 0 or 1
* match 0 or more
$ match the end of a string
^ match the beginning of a string
| either or
{} range or "Variance"
{x} expecting x amount

White Space Character:
\n new line
\s space
\t tab
\e escape
\f form feed
\r return 
'''

import re

exampleString = '''
Jessica is 15 years old, and Daniel is 27 years old.
Edward is 97, and his grandfather, Oscar, is 102.
'''

ages = re.findall(r'\d{1,3}',exampleString)
names = re.findall(r'[A-Z][a-z]*',exampleString)

print(ages, names)

ageDict = {}
x = 0
for eachName in names:
     ageDict[eachName] = ages[x]
     x += 1
print(ageDict)
