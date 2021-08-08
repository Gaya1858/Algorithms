'''
matrix multiplication can be done when the matrix A's row length equals to
matric B's column length. If A is 3x3 (RXC) B is 2X3 (R XC) len(AR) =len(BC)

A = a11,a12             B = b11,b12
    a21,a22                 b21,b22
C=AXB
c11 =a11*b11+a12*b21
c12 =a11*b12+a12*b22
c21 =a21*b11+a22*b21
c22 =a21*b12+a22*b22
there are 8 time multiplication done for 2X2 matrices

if the matrices are greater then 2X2 and powers of 2 then you can divide the matrices as 2X2 and do MM.
we can do the MM in 2 ways
    1. use for loop to do the process / or you recursively call the MM function if its greater than 2X2
        this time complexity is O(n^3)
    2. Strassen's Matric multiplication strategy uses only 7 multiplication process for 2X2
        and it's time complexity is O(n^2.81) which less then the other way

        Strassen's MM strategy:
        P =(A11+A22)*(B11+B22)
        Q =(A21+A22)*B22
        R =A11*(B12-B22)
        S =A22*(B21-B11)
        T =(A11+A12)*B22
        U =(A21-A11)*(B11+B12)
        V =(A12-A22)*(B21+B22)
        THEN
        C11 =P+S-T+V
        C12=R+T
        C21= Q+S
        C22=P+R-Q+U


'''
import math

a = [[2,4],[3,4]]
b =[[2,4],[3,4]]




def loopingThrough(a,b,n):
    c =[[],[]]
    for i in range(0,n):
        print(i)
        for j in range(0,n):
            print(j)
            for k in range(0,n,2):
                x = a[i][k]*b[k][j]
                y = a[i][k+1]*b[k+1][j]
                c[i].append(x+y)
                x =0
    return c

def split(a):
    row,col = math.floor(len(a)/2)

n =len(a)
c =loopingThrough(a,b,n)
print(c)