import sys
'''This below function checks the memory that the list taken when it was empty 
to filling up with integers'''
n=10
data =[]
for i in range(n):
    a =len(data)
    b =sys.getsizeof(data)
    print('Length: {0:3d}; Size of bytes: {1:4d}'.format(a,b))
    data.append(i)

'''
Length:   0; Size of bytes:   72
Length:   1; Size of bytes:  104
Length:   2; Size of bytes:  104
Length:   3; Size of bytes:  104
Length:   4; Size of bytes:  104
Length:   5; Size of bytes:  136
Length:   6; Size of bytes:  136
Length:   7; Size of bytes:  136
Length:   8; Size of bytes:  136
Length:   9; Size of bytes:  200
'''