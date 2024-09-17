import re

# a=re.compile(r'mo(o)?de')
# b1=a.search('asgfd hgas doie mode')
# b2=a.search('asgfd hgas doie moode')
# print(b1.group())
# print(b2.group())


# a=re.compile(r'mo(o)*de')
# b1=a.search('asgfd hgas doie mode')
# b2=a.search('asgfd hgas doie moooooode')
# print(b1.group())
# print(b2.group())


# a=re.compile(r'mo(o)+de')
# b1=a.search('asgfd hgas doie moode')
# b2=a.search('asgfd hgas doie moooode')
# print(b1.group())
# print(b2.group())


# a=re.compile(r'mo{3}de')
# b1=a.search('asgfd hgas doie mooode')
# print(b1.group())


a=re.compile(r'mo{3,}de')
b1=a.search('asgfd hgas doie mooooooooode')
print(b1.group())