"""
The median is the middle value in an ordered integer list. 
If the size of the list is even, there is no middle value. So the median is the mean of the two middle values.

For examples, if arr = [2,3,4], the median is 3.
For examples, if arr = [1,2,3,4], the median is (2 + 3) / 2 = 2.5.
You are given an integer array nums and an integer k. There is a sliding window of size k which is moving from the very left of the array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position.

Return the median array for each window in the original array. Answers within 10-5 of the actual value will be accepted.


Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
Output: [1.00000,-1.00000,-1.00000,3.00000,5.00000,6.00000]
Explanation: 
Window position                Median
---------------                -----
[1  3  -1] -3  5  3  6  7        1
 1 [3  -1  -3] 5  3  6  7       -1
 1  3 [-1  -3  5] 3  6  7       -1
 1  3  -1 [-3  5  3] 6  7        3
 1  3  -1  -3 [5  3  6] 7        5
 1  3  -1  -3  5 [3  6  7]       6



Input: nums = [1,2,3,4,2,3,1,4,2], k = 3
Output: [2.00000,3.00000,3.00000,3.00000,2.00000,3.00000,2.00000]
"""




class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        medians, window = [], []
        for i in range(len(nums)):
            # Find position where outgoing element should be removed from
            if i >= k:
              # window.remove(nums[i-k])        # this works too
              window.pop(bisect.bisect(window, nums[i - k]) - 1)

            # Maintain the sorted invariant while inserting incoming element
            bisect.insort(window, nums[i])

            # Find the medians
            if i >= k - 1:
                medians.append(float((window[k // 2]
                if k & 1 > 0
                else(window[k // 2 - 1] + window[k // 2]) * 0.5)))

        return medians

    
class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        small = []
        large = []
        
        def move(h1, h2):
            val, indx = heappop(h1)
            heappush(h2, (-val, indx))
            
        def get_med(h1, h2, k):
	        return h2[0][0] * 1. if k & 1 else (h2[0][0]-h1[0][0]) / 2.

        res = []
        for i in range(k):
            heappush(small, (-nums[i], i))
        # large have more items.
        for i in range(k - k//2):
            move(small, large)
            
        res.append(get_med(small, large, k))
        for i in range(k, len(nums)):
            if nums[i] >= large[0][0]:           
                heappush(large, (nums[i], i))
                if nums[i-k] <= large[0][0]:            
                    move(large, small)
            else:
                heappush(small, (-nums[i], i))
                if nums[i-k] >= large[0][0]:            
                    move(small, large)
            # print(small, large)
            while small and small[0][1] + k <= i:
                heappop(small)
            while large and large[0][1] + k <= i:
                heappop(large)
            res.append(get_med(small, large, k))
        return res
