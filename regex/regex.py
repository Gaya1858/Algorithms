'''
first we have to create a pattern using re.compile("ab") method
second create matcher using the pattern and pass in the string to find the pattern
match = pattern.finditr("abanabanababan")

'''

import re

s ='aaadaa'

k ="aa"
pattern = re.compile(k)
m = re.search(pattern, s)

if m == None: print("(-1, -1)")
while m:
    print(f"({m.start()},{m.end()-1})")
    m = pattern.search(s,m.start()+1)

# while count<len(s):
#     m=pattern.match(s[count:])
#     if(m != None):
#         print("(",m.start(),",",m.end()-1,")")
#     else:
#         print("(-1,-1)")
#     count+=1





pattern = re.compile('ba')

print(type(pattern))

matcher = pattern.finditer("abaababa")
for i in matcher:
    print('start:{}, end:{},group:{}' .format(i.start(),i.end(),i.group()))
    # start:1, end:3,group:ba
    # start:4, end:6,group:ba
    # start:6, end:8,group:ba
    # print("match is availabel at start index: ",i.group())
    # # match is availabel at start index:  ba
    # # match is availabel at start index:  ba
    # # match is availabel at start index:  ba
    # print("match is availabel at start index: ",i.start())
    # # match is availabel at start index:  1
    # # match is availabel at start index:  4
    # # match is availabel at start index:  6
    # print("match is availabel at start index: ",i.end()) # end method will return end index+1
    # # match is availabel at start index:  3
    # # match is availabel at start index:  6
    # # match is availabel at start index:  8
# match1 = re.match('ab','abaabaaabaaaa')
#
# for i in match1:
#     print(i.start(),i.group())

# s =input('Enter pattern to check:')
# m =re.match(s,'abcdefgh')

# if m != None:
#     print("Match is availabel at the beginning of the strinbg")
#     print('start index: {} and end index: {}'.format(m.start(),m.end()))
# else:
#     print("Match is not availabel at the beginning of the string")

# s =re.sub("\d",'#','a2c3v4b5n')
# print(s)
# s =re.subn("\d",'#','a2c3v4b5n')
# print(s)
#
# l = re.split('-','10-20-30-40-50')
# print(l)
