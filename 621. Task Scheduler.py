"""
Given a characters array tasks, representing the tasks a CPU needs to do, where each letter represents a different task. Tasks could be done in any order. Each task is done in one unit of time. For each unit of time, the CPU could complete either one task or just be idle.

However, there is a non-negative integer n that represents the cooldown period between two same tasks (the same letter in the array), that is that there must be at least n units of time between any two same tasks.

Return the least number of units of times that the CPU will take to finish all the given tasks.

Eg:
Input: tasks = ["A","A","A","B","B","B"], n = 2
Output: 8
Explanation: 
A -> B -> idle -> A -> B -> idle -> A -> B
There is at least 2 units of time between any two same tasks.
"""


# sol: https://leetcode.com/problems/task-scheduler/discuss/2609137/Python-Solution

class Solution:
    def leastInterval(self, tasks, n):
        curr_time, h = 0, []
        for v in collections.Counter(tasks).values():
            heapq.heappush(h, -1*v)
        while h:
            temp = []
            for _ in range(n+1):
                curr_time += 1
                if h:
                    x = heapq.heappop(h)
                    if x != -1:

                        temp.append(x+1)
                if not h and not temp:#not temp, add idle
                    break
            for item in temp:
                heapq.heappush(h, item)
        return curr_time

    
    
import heapq, collections
class Solution:
    #T=O(nm),S=O(n)
    #n=number of tasks 
    #m=idle time
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks) #{"A":3,"B":2}
        max_heap = [-f for f in count.values()]
        heapify(max_heap)
        q = deque()
        time = 0
        
        while q or max_heap:
            time += 1
            if max_heap:
                frequency = 1 + heappop(max_heap)
                if frequency:
                    q.append([frequency, time + n])
            
            if q and q[0][-1] == time:
                heappush(max_heap, q.popleft()[0])
        return time

