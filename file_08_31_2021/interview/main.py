

x ='I love 2 go 2 shops in we3k'

nums =[y for y in x if y.isnumeric() ]
new = ''.join(nums)
print(type(new))
#if-else condition in list comprehension

lis =[5,3,10,18,6,7]
new_lis =[x if x%2==0 else 10*x for x in lis]
print(new_lis)

#if-else condition in list comprehension

# nested loop ietratin for 2d arrays using list comprehension

a =[[1,  0, 12, -1 ],
    [7, -3,  2,  5],
    [-5, -2,  2, -9]]
new_a =[w for b in a for w in b]

print(new_a)

