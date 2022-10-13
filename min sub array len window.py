def minSubArrayLen(target: int, arr: list) -> int:
    """
    Find minimal length of a contiguous subarray
    target < sum of sub-aray
    """
    start = 0
    end = 0
    L = len(arr)
    sums = arr[0]
    mins = float("inf")

    while end < L:
        if sums >= target:
            mins = min(mins, end - start + 1)
            sums = sums - arr[start]
            start += 1
        else:
            end += 1
            if end == L:
                break
            sums = sums + arr[j]

    if mins == float("inf"):
        mins = 0

    return mins
