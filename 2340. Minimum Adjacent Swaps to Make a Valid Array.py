"""
You are given a 0-indexed integer array nums.

Swaps of adjacent elements are able to be performed on nums.

A valid array meets the following conditions:

The largest element (any of the largest elements if there are multiple) is at the rightmost position in the array.
The smallest element (any of the smallest elements if there are multiple) is at the leftmost position in the array.
Return the minimum swaps required to make nums a valid array.


Input: nums = [3,4,5,5,3,1]
Output: 6
Explanation: Perform the following swaps:
- Swap 1: Swap the 3rd and 4th elements, nums is then [3,4,5,3,5,1].
- Swap 2: Swap the 4th and 5th elements, nums is then [3,4,5,3,1,5].
- Swap 3: Swap the 3rd and 4th elements, nums is then [3,4,5,1,3,5].
- Swap 4: Swap the 2nd and 3rd elements, nums is then [3,4,1,5,3,5].
- Swap 5: Swap the 1st and 2nd elements, nums is then [3,1,4,5,3,5].
- Swap 6: Swap the 0th and 1st elements, nums is then [1,3,4,5,3,5].
It can be shown that 6 swaps is the minimum swaps required to make a valid array.

"""


# simple maths
def minimumSwaps(self, nums):
    smallest, largest = min(nums), max(nums)
    
    small_idx = min([i for i in range(len(nums)) if nums[i] == smallest])
    large_idx = max([i for i in range(len(nums)) if nums[i] == largest])
    
    if small_idx < large_idx:
        return small_idx + len(nums) - 1 - large_idx
    elif small_idx > large_idx:
        return small_idx - 1 + len(nums) - 1 - large_idx
    else:
        return 0

 
# Greedy ...............................................
# When smallest index lies beyond the largest we need one less swap because there would be an overlap of 1 swap

class Solution:
    def minimumSwaps(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return 0
        
        largest = 0
        smallest = 0
        
        for i in range(len(nums)):
            if nums[i] >= nums[largest]:
                largest = i
                
            if nums[i] < nums[smallest]:
                smallest = i
                
        ans = len(nums) - largest - 1 + smallest 

        
        return ans - (smallest > largest)


