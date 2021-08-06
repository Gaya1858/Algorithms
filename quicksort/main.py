'''
Quick sort
It is an inplace sort (you don't need a new object to sort elements)
it's best cae is O(logn) when the partitioning is in the middle(pivot should be in the middle
    it means left side of the pivot is smaller and right of if greater than the pivot.
    it is not possible all the time.
It's worst case if O(n^2)- partitioning will happen at the beginning or at any point
Partition Procedure:
    1. bring the pivot to the appropriate position such that left of the pivot smaller and right is larger
    2. quick sort left side
    3. quick sort right side

'''
array = [10,16,8,12,15,6,3,9,5]
def partition_func(low,high,lst):
    pivot = low
    pivot_value =lst[pivot]
    while(low<high):
        while (low<len(lst) and lst[low] <= pivot_value):
            low +=1
        while(lst[high] >pivot_value ):
            high -=1
        if(low <high):
            lst[low],lst[high] = lst[high],lst[low]
    lst[high],lst[pivot] =lst[pivot],lst[high]
    return high
def quick_sort(low,high,lst):
    if(low< high):
        part =partition_func(low,high,lst)

        quick_sort(low,part,lst)
        quick_sort(part+1,high,lst)

quick_sort(0, len(array) - 1, array)

print(f'Quick Sorted array: {array}')



