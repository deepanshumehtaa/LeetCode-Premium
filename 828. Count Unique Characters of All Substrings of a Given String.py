# AMAZON

"""
Let's define a function countUniqueChars(s) that returns the number of unique characters on s.


Example 1:

Input: s = "ABC"
Output: 10
Explanation: All possible substrings are: "A","B","C","AB","BC" and "ABC".
Every substring is composed with only unique letters.
Sum of lengths of all substring is 1 + 1 + 1 + 2 + 2 + 3 = 10
Example 2:

Input: s = "ABA"
Output: 8
Explanation: The same as example 1, except countUniqueChars("ABA") = 1.
Example 3:

Input: s = "LEETCODE"
Output: 92

"""

class Solution:
	def uniqueLetterString(self, s: str) -> int:
		prev = [-1] * len(s)
		nex = [len(s)] * len(s)

		index = {}
		for i, c in enumerate(s):
			if c in index:
				prev[i] = index[c]    
			index[c] = i

		index = {}
		for i in range(len(s) - 1, -1, -1):
			if s[i] in index:
				nex[i] = index[s[i]]
			index[s[i]] = i

		res = 0
		for i, c in enumerate(s):
			res += (nex[i] - i) * (i - prev[i])

		return res
  
  
  
  
  
  def uniqueLetterString(self, s):
    res, dict1 = [0], defaultdict(list)
    
    for i,c in enumerate(s):
        dict1[c].append(i)
        
    for key, val in dict1.items():
        for i in range(len(val)):
            idx = val[i]
            prev = val[i-1] if i-1>=0 else -1
            succ = val[i+1] if i+1<len(val) else len(s)
            res.append(res[-1] + (idx-prev)*(succ-idx))
        
    return res[-1]
  
  
  # DP
  def uniqueLetterString(self, s):
    # Let dp(i) be the answer for the substring ending at index i.
	
    prev, curr, dp = defaultdict(int), defaultdict(int), [0]
    
    for i,c in enumerate(s):
        curr[c] = i - prev[c] + 1
        dp.append(dp[-1] + sum(curr.values()))
        prev[c] = i + 1
        
    return dp[-1]
