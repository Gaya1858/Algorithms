'''Customer 1: Purchased size 6 shoe for $55.
Customer 2: Purchased size 6 shoe for $45.
Customer 3: Size 6 no longer available, so no purchase.
Customer 4: Purchased size 4 shoe for $40.
Customer 5: Purchased size 18 shoe for $60.
Customer 6: Size 10 not available, so no purchase.

'''
from collections import Counter
n =10
arr ='2 3 4 5 6 8 7 6 5 18'
x =6
shoe =[[6,55],[6,45],[6,55],[4,40],[18,60],[10,50]]

num_shoes =10
shoe_size ='2 3 4 5 6 8 7 6 5 18'
shoe_size =shoe_size.split()
shoe_size =Counter(shoe_size)
cus_need =6
total =0
# for i in range(cus_need):
#     value =input().split()
#     size =(value[0])
#     price =int(value[1])
#     if(size in shoe_size.keys()):
#         if(shoe_size[size] >=1):
#             total +=price
#             shoe_size[size] -=1
# print(total)



a = {5, 9, 2, 4}
b = {11, 12, 2, 4}
new_list =sorted(a^b)

for i in new_list:
    print(i)

'''4           set a size M = 4
2 4 5 9     a = {2, 4, 5, 9}'
4           set b size N = 4
2 4 11 12   b = {2, 4, 11, 12}'''