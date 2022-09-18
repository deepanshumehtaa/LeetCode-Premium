from collections import Counter


def characterReplacement(s: str, k: int) -> int:
    """
    Just to return the length of longest substring after the k alterations.

    Algo:
    Sliding window with (start, end)
    window_size = end - start + 1

    1. expand the window and count the chars for most occuring char
    2. if window_size - most_frequent_value > k, start shrinking the window
    3. the max size window attained during this process is the answer
    """

    start = end = 0  # both ptr will move
    counter = Counter()

    res = 0
    while end < len(s):
        counter[s[end]] = counter.get(s[end], 0) + 1

        # The start ptr of window will move right, if the
        while end - start + 1 - counter.most_common(1)[0][1] > k:
            counter[s[start]] -= 1
            start += 1

        res = max(end - start + 1, res)
        end += 1

    return res

"""
Test case:

1. s="BAAAB", k=2 ---> 5
2. s="ABABAAABA", k=2 ---> 7
"""