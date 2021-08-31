import re

# s =input ("Enter identifier to check:")
#
# m=re.fullmatch('[a-k][0369][a-zA-Z0-9#]*',s)
# if m != None:
#     print(" yes it is valued identifier")
# else:
#     print("Not vlaued")

#*************************
# checking that the string starting and ending with same character

y='abba'
reg = r'^[a-z]$|^([a-z]).*\1$'
s = re.search(reg,y)
if( s!= None):
    print("Valid")
else:
    print("invalid")

s =re.search(r'^([a-z]).*\1$','a*a')
print(s!=None)