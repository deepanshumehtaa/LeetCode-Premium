import heapq


def best_priority_queue(arr):
    """
    [[2, 10], [4, 10], [10, 20], [10, 30]]
    expected answer: 2
    """
    arr.sort(key=lambda x: x[0])  # inplace sorting
    pq = []  # priority queue

    count = 0
    for start, end in arr:
        while pq and pq[0] <= start:
            heapq.heappop(pq)  # return the min value from the heap, and maintaining the heap property
        else:
            heapq.heappush(pq, end)  # appending num to pq and apply heapify on pq
            count = max(count, len(pq))

    return count


arr = [[2, 10], [4, 10], [10, 20], [10, 30]]  # already sorted
rooms = best_priority_queue(arr)
print(rooms)
