"""
# Tweet Counts Per Frequency
# https://leetcode.com/problems/tweet-counts-per-frequency/

Analyzing the number of tweets that occur in select periods of time.
These periods can be partitioned into smaller time chunks based on a certain frequency(every minute, hour, or day).


For example:
the period [10, 10000] (in seconds) would be partitioned into the following time chunks with these frequencies:
Every minute: [10,69], [70,129], ..., [9970,10000]
Every Day: [10,10000]

minute chunk: 60s interval
hour chunk: 3600s interval
day chunk: 86400s interval


Ex1:
["TweetCounts","recordTweet","recordTweet","recordTweet","getTweetCountsPerFrequency","getTweetCountsPerFrequency","recordTweet","getTweetCountsPerFrequency"]
[[],["tweet3",0],["tweet3",60],["tweet3",10],["minute","tweet3",0,59],["minute","tweet3",0,60],["tweet3",120],["hour","tweet3",0,210]]
o/p:
[null,null,null,null,[2],[2,1],null,[4]]


Ex2:
["TweetCounts","recordTweet","recordTweet","recordTweet","recordTweet","recordTweet","getTweetCountsPerFrequency","recordTweet","recordTweet","recordTweet","getTweetCountsPerFrequency","recordTweet","recordTweet"]
[[],["tweet0",12],["tweet1",39],["tweet2",81],["tweet3",11],["tweet4",45],["day","tweet2",11,1532],["tweet3",14],["tweet4",90],["tweet3",13],["hour","tweet2",14,2203],["tweet4",87],["tweet2",74]]
o/p:
[null,null,null,null,null,null,[1],null,null,null,[1],null,null]
"""
import math
# from bisect import insort, bisect_left, bisect_right
from collections import defaultdict
from typing import List


class TweetCounts:
    """solved using a dict"""

    def __init__(self):
        self.dic = defaultdict(lambda: [])  # defaultdict(list)

    def record_tweet(self, hash_tag: str, time: int) -> None:
        self.dic[hash_tag].append(time)

    def tweet_counts_per_frequency(self, freq: str, hash_tag: str, startTime: int, endTime: int) -> List[int]:
        """
        freq: like choice field in db ('minute', 'hour', 'day')
        """
        chunk = 60
        if freq == "hour":
            chunk = 3600
        elif freq == "day":
            chunk = 86400

        num_of_chunk = math.ceil((endTime - startTime) / chunk)

        # as we are ceil our num_of_chunk is round-off so, for exact num_of_chunk
        if (endTime - startTime) % chunk == 0:
            num_of_chunk += 1

        res = [0] * num_of_chunk
        timeLst = self.dic[hash_tag]

        for time in timeLst:
            if time >= startTime and time <= endTime:
                time -= startTime
                res[time // chunk] += 1

        return res

# Your TweetCounts object will be instantiated and called as such:
# obj = TweetCounts()
# obj.recordTweet(tweetName, time)
# param_2 = obj.getTweetCountsPerFrequency(freq,tweetName,startTime,endTime)
