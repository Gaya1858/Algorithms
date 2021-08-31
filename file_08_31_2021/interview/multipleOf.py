
import math
import random
from timeit import timeit


def multiple(n,m):
    if (m%n ==0):
        return True
    else:
        return False
def minmax(lit):
    min = lit[0]
    for i in lit:
        if(i< min):
            min =i
    return min
def sum_squre(n):
    x =sum([x**2 for x in range(n)])
    return x
def sum_odd(n):
    x = sum([x**2 for x in range(n) if x%2 ==1])
    return x
def slice(string):
    for i in range(-1,-len(string)-1,-1):
        k= i+len(string)
        print(string[i],string[k])

def choice_ran(data):
    return data[random.randrange(len(data))]

def revsere1(lis):
    m =[lis[x] for x in range(-1,-len(lis)-1,-1)]
    return m
def reverse2(list):
    temp=0
    length=len(list)
    if length%2:
        mid=(length-1)//2
        for i in range(mid):
            temp=list[i]
            list[i]=list[-i-1]
            list[-i-1]=temp
    else:
        mid=length//2
        for i in range(mid):
            temp=list[i]
            list[i]=list[-i-1]
            list[-i-1]=temp
    return list
def list_com():
    x =[x*(x+1) for x in range(10)]
    return x
def aplha():
    x =[chr(y) for y in range(97,97+26)]
    return x
# print(multiple(3,12))
# print(multiple(43,9))
# print(minmax([94,3746,98,1,267,3873,87,0.5]))
# print(sum_squre(10))
# print(sum_odd(10))
# print(slice("Gaya"))
#
# x =[2**x for x in range(9)]
# print(x)
# print(revsere1([94,3746,98,1,267,3873,87,0.5]))
# c =[94,3746,98,1,267,3873,87,0.5]
# print(reverse2(c))
# print(list_com())
# print(aplha())

def sum_num(n):
    x =sum([x for x in range(n+1)])
    return x
def sum_num2(n):
    return (n*(n+1))/2

a =[1,2,3,4,5]
b = a
a[0] =10
print("b[0]:",b[0],"a[0]: ",a[0])
class Obj:
    def __int__(self):
        self.name ="Gaya"
        self.age =20

n_obj =Obj()
m_obj = n_obj
n_obj.age=30
print(n_obj.age,m_obj.age)