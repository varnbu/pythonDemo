import re

p = re.compile('ab*c')
print(p.match('abbbbbbbbc'))