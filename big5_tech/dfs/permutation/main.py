def permute(nums):

    result =[]
    if len(nums) ==1:
        print("i am from if: ",nums)
        return [nums[:]]
    for i in range(len(nums)):
        val =nums.pop(0)

        remArray =permute(nums)
        for perm in remArray:
            perm.append(val)
        result.extend(remArray)
        nums.append(val)


    return result

for i in permute([1,2,3]):
    print(i)
'''
Runtime: 31 ms, faster than 96.92% of Python3 online submissions for Permutations.
Memory Usage: 14.2 MB, less than 97.47% of Python3 online submissions for Permutations.
'''