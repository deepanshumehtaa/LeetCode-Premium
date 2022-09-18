"""
Given an array of n integers nums and an integer target,
find the number of index triplets i, j, k with 0 <= i < j < k < n that
satisfy the condition nums[i] + nums[j] + nums[k] < target.


Input: nums = [-2,0,1,3], target = 2
Output: 2
Explanation: Because there are two triplets which sums are less than 2:
[-2,0,1]
[-2,0,3]
"""


class Solution:
    def two_ptr_clean(self, nums: list, target: int):
        def twosmaller(nums, startidx, target):
            su = 0
            left = startidx
            right = len(nums) - 1
            while (left < right):
                if (nums[left] + nums[right] < target):
                    su += right - left
                    left += 1
                else:
                    right -= 1
            return su

        nums.sort()
        su = 0
        for i in range(0, len(nums) - 2):
            su += twosmaller(nums, i + 1, target - nums[i])
        return su

    def two_ptr(self, nums: list, target: int) -> int:
        nums = sorted(nums)
        n = len(nums)
        right = n - 1
        ans = 0
        for i in range(n):
            t = target - nums[i]
            left = i + 1
            right = n - 1
            while left < right:
                temp = nums[left] + nums[right]
                if temp < t:
                    ans += right - left
                    left += 1
                elif temp >= t:
                    right -= 1
        return ans
