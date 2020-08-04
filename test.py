# Python3
import re

searchstring = ('hello, HELLO, helLO')

myregex = re.compile(r'hel')
result = myregex.sub('HEL', searchstring)
print(result)

re.compile(r'''(
    (\d{3}|\(\d{3}\))   #area code
    \d{4}               #last 4 digits
)''', re.VERBOSE)
