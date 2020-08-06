# Python3

import re

myregex = re.compile(r'\d{3}')
result = myregex.search('415')
print(result.group())
