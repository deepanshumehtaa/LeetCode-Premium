"""
Input: ribbons = [9,7,5], k = 3
Output: 5
Explanation:
- Cut the first ribbon to two ribbons, one of length 5 and one of length 4.
- Cut the second ribbon to two ribbons, one of length 5 and one of length 2.
- Keep the third ribbon as it is.
Now you have 3 ribbons of length 5.


Input: ribbons = [7,5,9], k = 4
Output: 4
Explanation:
- Cut the first ribbon to two ribbons, one of length 4 and one of length 3.
- Cut the second ribbon to two ribbons, one of length 4 and one of length 1.
- Cut the third ribbon to three ribbons, two of length 4 and one of length 1.
Now you have 4 ribbons of length 4.


Input: ribbons = [5,7,9], k = 22
Output: 0
Explanation: You cannot obtain k ribbons of the same positive integer length.
"""


# premiun

class Solution:
    def maxLength(self, ribbons: List[int], k: int) -> int:
        
        def can_obtain(l, ribbons):
            total = 0
            for r in ribbons:
                total += r // l
            return total
        
        # find the largest l that meets k
        
        left = 0 
        right = max(ribbons)
        while left < right:
            # mid is right side
            mid = left + (right - left + 1) //2
            if can_obtain(mid, ribbons) >= k:
                left = mid 
            else:
                right = mid - 1
        return left
