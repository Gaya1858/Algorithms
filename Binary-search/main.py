'''
binary search:
given a sorted list you can search a key
list =[17,21,35,57,68]
key =18
let's take lower inder, higher index and middle index
low =0, high =lenofthelist(4) , mid =low+hig/2 wchich is (2)
check- what is on the middle index, lower inder and higher index compare with the key
--- if not matching then check with just mid index value, if mid value is less then key
    make low = mid-1 and high same.
    now low=2-1=1, high =4 mid =1+2/2 =1
if mid value is greaterthan then key
    low = same, high= mid-1 mid = l+h/2

'''
import math


def binary_search(arr,start,end,key):
    mid = math.floor((start+end)/2)
    if start<end:
        if arr[start]==key:
            return start
        elif arr[end] == key:
            return end
        elif key >arr[end]:
            return None
        elif arr[mid] ==key:
            return mid
        elif key <arr[start]:
            return None
        elif arr[mid] <key:
            return binary_search(arr,start,end,key)
        else:
            end=mid-1
            return binary_search(arr,start,end,key)


arr = [ 2, 3, 4, 10, 40 ]
ind =binary_search(arr,0,len(arr)-1,2)
if(ind != None):
    print(f"Index is {ind} and the value is {arr[ind]}")
else:
    print("the key doesn't exist int the list")
