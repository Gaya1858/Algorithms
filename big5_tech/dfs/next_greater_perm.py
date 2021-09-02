def reverse(nums, x):
    m  =x
    for i in range(len(nums)-1,x,-1):
        if m <i:
            nums[m],nums[i] = nums[i],nums[m]
            m+=1
        else:
            break

    return nums

def n_perm(nums):
    if len(nums) ==1:
        return nums
    if len(nums) ==2:
        nums[0],nums[1] =nums[1],nums[0]
        return nums
    x =len(nums)-2
    while x >=0 and nums[x] >= nums[x+1]:
        x -=1
    print(x)

    nums =reverse(nums,x+1)
    if x ==-1:
        return
    m =x+1
    while m < len(nums) and nums[m] <=nums[x]:
        m +=1
    nums[m],nums[x]=nums[x],nums[m]

    return nums


nums = [5,4,7,5,3,2]
#nums =sorted(nums)
print(nums)
print(n_perm(nums))
#[5,5,2,3,4,7]