import re

p = re.compile(r'(\d+)-(\d+)-(\d+)')
#  完全匹配
a = re.match(p, '2019-10-09').group()
a1 = re.match(p, '2019-10-09').group(2)
a3 = re.match(p, '2019-10-09').groups()
aa, ab, ac = re.match(p, '2019-10-09').groups()
print(a)
print(a1)
print(a3)
print(aa, ab, ac)
#  搜索
print(p.search('aa2019-09-19'))
