'''
there are  two ways of doing this sort:
    1. 2-way merge sort - which is done by iteratively
    2. merge sort - which is done by recursively
time complexity is O(nlogn)
space compleity is O(n+nlogn) --- O(n)
pros:
    can be done in large size of lists like millions of elements in it
    more suitable for linked lists.As it doesn't need to create another LL. extra space is not needed
    External sorting
    stable sorting algo. doesn't change the order if two elements are equal.
cons:
    will be very slow when used n<=15
    extra space (not inplace sort)
    recursive algo which can use stack memory of logn
'''
# Merge two sorted sublists `A[frm…mid]` and `A[mid+1…to]`
import math


def merge(A, temp, frm, mid, to):

    k = frm
    i = frm
    j = mid + 1

    # loop till no elements are left in the left and right runs
    while i <= mid and j <= to:
        if A[i] < A[j]:
            temp[k] = A[i]
            i = i + 1
        else:
            temp[k] = A[j]
            j = j + 1

        k = k + 1

    # copy remaining elements
    while i < len(A) and i <= mid:
        temp[k] = A[i]
        k = k + 1
        i = i + 1

    ''' no need to copy the second half (since the remaining items
        are already in their correct position in the temporary array) '''

    # copy back to the original list to reflect sorted order
    for i in range(frm, to + 1):
        A[i] = temp[i]


# Iteratively sort sublist `A[low…high]` using a temporary list
def mergesort(A):

    low = 0
    high = len(A) - 1

    # sort list `A` using a temporary list `temp`
    temp = A.copy()

    # divide the list into blocks of size `m`
    # m = [1, 2, 4, 8, 16…]

    m = 1
    while m <= high - low:

        # for m = 1, i = [0, 2, 4, 6, 8…]
        # for m = 2, i = [0, 4, 8, 12…]
        # for m = 4, i = [0, 8, 16…]
        # …

        for i in range(low, high, 2*m):
            frm = i
            mid = i + m - 1
            to = min(i + 2*m - 1, high)
            merge(A, temp, frm, mid, to)

        m = 2*m
# Recursive Python Program for merge sort

def merge1(left, right):
    if not len(left) or not len(right):
        return left or right

    result = []
    i, j = 0, 0
    while (len(result) < len(left) + len(right)):
        if left[i] < right[j]:
            result.append(left[i])
            i+= 1
        else:
            result.append(right[j])
            j+= 1
        if i == len(left) or j == len(right):
            result.extend(left[i:] or right[j:])
            break

    return result

def mergesort1(list):
    if len(list) < 2:
        return list

    middle = math.floor(len(list)/2)
    left = mergesort1(list[:middle])
    right = mergesort1(list[middle:])

    return merge1(left, right)


# Iterative implementation of merge sort
if __name__ == '__main__':

    A = [5, 7, -9, 3, -4, 2, 8]
    b =[5, 7, -9, 3, -4, 2, 8]
    print("Original array:", A)
    mergesort(A)

    print("Modified array:", A)
    print("Recursively Modified array:", mergesort1(b))
