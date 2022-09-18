"""
360. Sort Transformed Array
"""


class Solution:
    def findMaxConsecutiveOnes(self, nums: list) -> int:
        """
        `codefarm`
        eg: [1,0,1,1,1,0,0,1] --> 5
        """
        return self.best_sliding_window(nums)
        # return self.sexy_window(nums)

    def best_sliding_window(self, nums) -> int:
        """Good One"""
        # TIME COMPLEXITY : O(N)
        # SPACE COMPLEXITY : O(1)

        start, end = 0, 0
        maxLen = 0
        k = 1  # atmost 0s flip
        while end < len(nums):

            if nums[end] == 0:
                k -= 1

            print(nums[end], k)
            if k < 0:
                # when k less than 0, no need to shrink window, just slide the window by start + 1 and end + 1
                if nums[start] == 0:
                    k += 1
                start, end = start + 1, end + 1
                continue

            if nums[end] == 1 or k >= 0:
                maxLen = max(maxLen, end - start + 1)

            end += 1
        return maxLen

    def sexy_window(self, nums) -> int:
        zeroCount = 0  # Keeps track of current total 0s
        oneCount = 0  # Keeps track of current total 1s
        maxOnes = 0  # Max amount of consecutive ones found
        windowStart = 0

        for windowEnd in range(len(nums)):
            num = nums[windowEnd]
            if num == 0:
                zeroCount += 1
            else:
                oneCount += 1

            while zeroCount > 1:
                remove = nums[windowStart]
                if remove == 0:
                    zeroCount -= 1
                else:
                    oneCount -= 1
                windowStart += 1

            maxOnes = max(maxOnes, windowEnd - windowStart + 1)
        return maxOnes
