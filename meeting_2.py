"""
Meeting Rooms2
Given an array of meeting time intervals intervals where intervals[i] = [starti, endi], return the minimum number of conference rooms required.

Ex:
Input: intervals = [[0,30],[5,10],[15,20]]
Output: 2
"""


import heapq


from queue import PriorityQueue


class Solution:
    """
    [[2,10],[4,10],[10,20],[10,30]]
    
    The Another Question would be:
    How many Events you can attend
    https://leetcode.com/problems/maximum-number-of-events-that-can-be-attended/
    """
    def minMeetingRooms(self, intervals):
        """
        time complexity O(n log(n))
        Sort all time points and label the start and end points. 
        Move a vertical line from left to right.
        When it meets a start point, curr_rooms += 1.
        When it meets an end point, curr_rooms -= 1.
        
        if there is a tie: put end point before start point.
        Update the maximal occupied rooms during the move.
        """
        
        # return self.priority_queue(intervals)
        return self.best_priority_queue(intervals)
        
        start = sorted([s for s, e in intervals])
        end = sorted([e for s, e in intervals])
        
        # Can't use .sort here as it does't return anything + inplace operator
        # start = intervals.sort(key=lambda x:x[0])
        
        res, count = 0, 0
        s, e = 0, 0
        
        while s < len(start):
            if start[s] < end[e]:
                count += 1
                s += 1
            else:
                count -= 1
                e += 1
                
            res = max(res, count)
        
        return res
    
    def using_heap(self, arr):
        """
        we are only saving the endtime in the heap.
        """
        arr.sort(key = lambda x : x[0])
        pq = []
        
        count = 0
        for start, end in arr:
            while pq and pq[0] <= start:
                heapq.heappop(pq)
            else:
                heapq.heappush(pq, end)
                count = max(count, len(pq))
                print(">>>")
        
        return count
    
    def best_priority_queue(arr):
        """we are only saving the endtime in the heap."""
        arr.sort(key=lambda x: x[0])
        pq = []

        max_ = 1
        for start, end in arr:
            if pq:
                if pq[0] > start:  # overlapping condition
                    heapq.heappush(pq, end)
                    max_ = max(max_, len(pq))
                else:
                    heapq.heappop(pq)  # no overlapping meand smallest meeting has been over.
            else:
                pq.append(end)  # appending end time

        return max_
    
    def priority_queue1(self, intervals):
        """
        """
        # sort by start times so we select meetings in order of start times
        # and this makes intuation and comparing easy
        intervals.sort()
        
        # keep a priority queue of end times available
        mq = PriorityQueue()
        
        if intervals:
            mq.put(intervals[0][1])
            
        for i in range(1, len(intervals)):
            if not mq.empty():
                end = mq.get()
                # first available meeting end time conflicts
                # so we need to keep this existing meeting in a separate room
                # in addition to the meeting we are currently checking
                if end > intervals[i][0]:
                    mq.put(end)
                    # always add current meeting's end time to indicate a booking
                mq.put(intervals[i][1])

        return mq.qsize()
