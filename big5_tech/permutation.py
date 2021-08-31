"""Approach 1: Backtracking

Backtracking is an algorithm for finding all solutions by exploring all potential candidates. If the solution candidate
turns to be not a solution (or at least not the last one), backtracking algorithm discards it by making some changes on
the previous step, i.e. backtracks and then try again.

Here is a backtrack function which takes the index of the first integer to consider as an argument backtrack(first).

If the first integer to consider has index n that means that the current permutation is done.
Iterate over the integers from index first to index n - 1.
Place i-th integer first in the permutation, i.e. swap(nums[first], nums[i]).
Proceed to create all permutations which starts from i-th integer : backtrack(first + 1).
Now backtrack, i.e. swap(nums[first], nums[i]) back.

"""


def permute(nums):
    if not nums:
        return []

    result = []
    perm = []
    unused = set(nums)
    def backTrack():
        if len(perm) == len(nums):
            result.append(perm[:])
            return result

        for num in list(unused):
            perm.append(num)
            unused.remove(num)
            backTrack()
            perm.pop()
            unused.add(num)

    backTrack()
    return result

nums =[1,2,3]

print(permute(nums))

#######################

def permute( nums):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """
    def backtrack(first = 0):
        # if all integers are used up
        if first == n:
            output.append(nums[:])
        for i in range(first, n):
            # place i-th integer first
            # in the current permutation
            nums[first], nums[i] = nums[i], nums[first]
            # use next integers to complete the permutations
            backtrack(first + 1)
            # backtrack
            nums[first], nums[i] = nums[i], nums[first]

    n = len(nums)
    output = []
    backtrack()
    return output
nums =[1,2,3]

print(permute(nums))