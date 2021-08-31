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


'''
n this task, a valid float number must satisfy all of the following requirements:
 Number can start with +, - or . symbol. 
For example: 

✔
+4.50 

✔
-1.0 

✔
.5 

✔
-.7 

✔
+.4 

✖
 -+4.5
 Number must contain at least  decimal value. 
For example: 

✖
 12. 

✔
12.0  
'''
f_ponit =r'^[+-.]?[0-9]*\.[0-9]+$'

# for i in range(int(input())):
#     print(bool(re.match(f_ponit,input())))

########### Group() returns one or more subgroups of the match

m =re.match(r'(\w+)@(\w+)\.(\w+)',"gayathri1858@yahoo.com")
if (m != None):
    print(m.group())
# group(0) or group() return entire string if it is true otherwise error
# you can also get subgroup like this group(1) 'gayathri1858'
'''
groups() return a tuplr containing all the subgroups of the match
'''
print(m.groups()) # ('gayathri1858', 'yahoo', 'com')
'''
groupdict() returns a dictionary containing all the names subgroups of the match 
keyed by the group name
'''
m =re.match(r'(?P<user>\w+)@(?P<website>\w+)\.(?P<extension>\w+)',"gayathri1858@yahoo.com")
print(m.groupdict()) #{'user': 'gayathri1858', 'website': 'yahoo', 'extension': 'com'}

# task is to find the first occurrence of an alphanumeric character in  (read from left to right)
# that has consecutive repetitions.

strin = '..12345678910111213141516171820212223'
pattern =r'([a-zA-Z0-9])\1+'
matc = re.search(pattern,strin.strip())
print(strin[matc.start()] if matc else -1)
print(matc.group(1) if matc else -1)

''' findall()  returns all the non-overlapping matches of patterns in a string 
as a list of strings
'''
print(re.findall(r'\w',"http://www.google.com/"))#['h', 't', 't', 'p', 'w', 'w', 'w', 'g', 'o', 'o', 'g', 'l', 'e', 'c', 'o', 'm']

'''
finditer() - returns an iteratoe yielding matchobject instances over all 
non -overlapping matches for the re pattern in the string
'''
sa=re.finditer(r'\w',"http://www.google.com/")

for i in sa:
    if i:
        print(i.group(),end=",")
print()
# chanllenge
'''
given a string . It consists of alphanumeric characters, spaces and symbols(+,-). 
Your task is to find all the substrings of  that contains  or more vowels. 
Also, these substrings must lie in between  consonants and should contain vowels only.
'''
strg ="rabcdeefgyYhFjkIoomnpOeorteeeeet"
consonants = 'qwrtypsdfghjklzxcvbnm'
vowels = 'aeiou'
match = re.findall(r'(?<=['+consonants+'])(['+vowels+']{2,})(?=['+consonants+'])',strg,flags =re.I)

if match:
    for i in match:
        print(i)
else:
    print (-1)
strg ="rabcdeefgyYhFjkIoomnpOeorteeeeet"
consonants = 'qwrtypsdfghjklzxcvbnm'
vowels = 'aeiou'
match = re.findall(r'(?<=['+consonants+'])(['+vowels+']{2,})(?=['+consonants+'])',strg,flags = re.I)
# if match:
#     for i in match:
#         print(i)
# else:
#     print(-1)
s=['11',
   'a = 1;',
    'b = input();',

    'if a + b > 0 && a - b < 0:',
    'start()',
    'elif a*b > 10 || a/b < 1:',
    'stop()',
    'print set(list(a)) | set(list(b))',
    '#Note do not change &&& or ||| or & or |',
    '#Only change those "&&" which have space on both sides.',
    '#Only change those "||" which have space on both sides.']

for i in range(len(s)):

    line =s[i]

    if '&&' in line:
        line.replace(' && ',' and ')
        print(line)
    elif'||' in line:
        line.replace(' || ',' or ')
        print(line)
    else:
        print(line)
