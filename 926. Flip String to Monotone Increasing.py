"""

A binary string is monotone increasing if it consists of some number of 0's (possibly none), followed by some number of 1's (also possibly none).

You are given a binary string s. You can flip s[i] changing it from 0 to 1 or from 1 to 0.

Return the minimum number of flips to make s monotone increasing.

 

Example 1:

Input: s = "00110"
Output: 1
Explanation: We flip the last digit to get 00111.
Example 2:

Input: s = "010110"
Output: 2
Explanation: We flip to get 011111, or alternatively 000111.
Example 3:

Input: s = "00011000"
Output: 2
Explanation: We flip to get 00000000.


"""



# DP

def minFlipsMonoIncr(self, s):
    count_one = 0 if s[0] == "0" else 1
        
    dp = [0]*len(s)
    
    for i in range(1,len(s)):
        if s[i] == "1":
            dp[i] = dp[i-1]
            count_one += 1
        else:
            dp[i] = min(dp[i-1] + 1, count_one)
            
    return dp[-1]
  
  
  # DP2
  
  class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        zeros = [float('inf') for _ in range(len(s))]
        ones = [float('inf') for _ in range(len(s))]
        
        if s[-1] == '0':
            zeros[-1] = 0
            ones[-1] = 1
        else:
            ones[-1] = 0
            zeros[-1] = 1
        
        for i in range(len(s)-2, -1, -1):
            if s[i] == '1':
                ones[i] = ones[i+1]
                zeros[i] = 1 + min(ones[i+1], zeros[i+1])
            else:
                ones[i] = 1 + ones[i+1]
                zeros[i] = min(ones[i+1], zeros[i+1])
        return min(zeros[0], ones[0])
      
      
  # DP3
  
  
  class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        
        # occurrence of 1 in strings s
        occ_of_1 = 0
        
        # counter of flips of 1->0 and 0->1
        flip = 0
        
        
        # scan each digit on substring s[:i], i = 1 ~ len(s)
        for char in s:
            
            if char == '1':
                
				# update occurrence of '1'
                occ_of_1 += 1
                
				# current digit is '1'
                # no need to flip when 1 is on the tail of current substring
            
            else:
                
				# current digit is '0'
                # need to flip when 0 is on the tail of current substring
                
                # option_1: flip current 0 to 1, keep leading digits, then substring is monotone increasing
                
                # option_2: flip leading 1s to 0s, keep current 0, then substring is monotone increasing
                
                # select optimal solution
                flip = min(flip+1, occ_of_1)
                
        return flip
