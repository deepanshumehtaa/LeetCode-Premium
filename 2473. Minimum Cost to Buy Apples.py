from heapq import heappop, heappush

def minimumCost(N: int, K: int, apples: List[int]) -> int:
    # Use a min heap to keep track of the cheapest packages of apples
    heap = []
    for i in range(N):
        # Add the price of the i-th package and its weight to the heap
        heappush(heap, (apples[i], i+1))

    # Initialize the total cost and the number of apples bought
    cost = 0
    bought = 0

    # Buy apples for K days
    for i in range(K):
        # Initialize the number of apples needed for the i-th day
        needed = K - bought

        # Buy the cheapest packages of apples until we have enough for the i-th day
        while heap and heap[0][1] <= i+1:
            heappop(heap)

        while heap and needed > 0:
            price, weight = heappop(heap)
            if weight > i+1:
                # We can only buy as much as we need for the i-th day
                cost += price * needed
                bought += needed
                needed = 0
                if weight > i+2:
                    # Store the remaining apples for future days
                    heappush(heap, (price, weight - (i+2)))
            else:
                # We can buy the whole package
                cost += price * (weight - (i+1))
                bought += weight - (i+1)

    return cost
