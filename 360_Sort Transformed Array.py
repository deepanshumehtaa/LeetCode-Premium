from typing import List

"""
Given a sorted integer array nums and three integers a, b and c,
apply a quadratic function of the form
f(x) = ax2 + bx + c to each element nums[i] in the array,
and return the array in a sorted order.

Ex1:
Input: nums = [-4,-2,2,4], a = 1, b = 3, c = 5
Output: [3,9,15,33]

Ex2:
Input: nums = [-4,-2,2,4], a = -1, b = 3, c = 5
Output: [-23,-5,1,7]
"""


def sortTransformedArray(self, nums: List[int], a: int, b: int, c: int) -> List[int]:
    for i, num in enumerate(nums):
        nums[i] = a * num * num + b * num + c

    arr = []
    i, j = 0, len(nums) - 1
    # upward increasing parabola
    if a > 0:
        while i <= j:
            if nums[i] > nums[j]:
                arr.append(nums[i])
                i += 1
            else:
                arr.append(nums[j])
                j -= 1
    elif a < 0:
        # downward increasing parabola
        while i <= j:
            if nums[i] < nums[j]:
                arr.append(nums[i])
                i += 1
            else:
                arr.append(nums[j])
                j -= 1
    else:
        # linear equation - line
        if b > 0:
            # positive slope
            return nums
        else:
            # negative slope
            return nums[::-1]

    return arr if a < 0 else arr[::-1]

