from typing import List


# DP solution
class Solution1:
    # @param num, a list of integer
    # @return an integer
    def rob(self, num):
        left = left_left = 0
        for i in range(len(num)):
            left, left_left = max(num[i] + left_left, left), left
        return left


class Solution2:
    cache = {}

    def rob(self, nums: List[int]) -> int:
        memo = {}

        def dfs(i):
            # see if we have already robbed this house
            if i in memo:
                return memo[i]

            # we have left the neigborhood and can't rob anymore
            if i >= len(nums):
                return 0

            # can rob current house but can't rob next
            rob_here = nums[i] + dfs(i + 2)

            # don't rob this house but instead rob the next
            rob_next = dfs(i + 1)

            memo[i] = max(rob_here, rob_next)
            print(memo)
            return memo[i]

        return dfs(0)


class Solution3:
    def rob(self, arr: List[int]) -> int:

        memo = {}

        def recurse(arr, l):  # max rob at array arr[l:]
            if l >= len(arr):
                return 0

            if l in memo:
                return memo[l]

            rob_first = arr[l] + recurse(arr, l + 2)
            rob_second = recurse(arr, l + 1)
            memo[l] = max(rob_first, rob_second)

            return memo[l]

        return recurse(arr, 0)


class Solution4:
    def rob(self, nums: List[int]) -> int:
        # Constant sliding window of 4 elements + memoization within the array

        # Early return corner cases
        if len(nums) <= 2:
            return max(nums)

        # 3rd element of the array for the sliding window
        nums[2] += nums[0]

        # Sliding window starts from the 4th element
        for i in range(3, len(nums)):
            print(nums, nums[i])

            # We are looking for the max of two elements before the previous element
            # This is to cover the cases such as [5, 1, 1, 5, 1, 1, 5]
            print(nums[i - 3], nums[i - 2])
            nums[i] += max(nums[i - 2], nums[i - 3])

        return max(nums[-1], nums[-2])


# old is Gold
class Solution5:
    def rob(self, nums):
        if len(nums) <= 0:
            return 0

        elif len(nums) == 1:
            return nums[0]

        elif len(nums) == 2:
            return max(nums[0], nums[1])

        else:
            cum_arr = [0] * len(nums)
            cum_arr[0] = nums[0]
            cum_arr[1] = max(nums[0], nums[1])

            for i in range(2, len(nums)):
                cum_arr[i] = max(cum_arr[i - 2] + nums[i], cum_arr[i - 1])

            print(cum_arr)
            return cum_arr[len(nums) - 1]
