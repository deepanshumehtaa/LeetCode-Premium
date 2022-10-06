"""

There is a new alien language that uses the English alphabet. However, the order among the letters is unknown to you.

You are given a list of strings words from the alien language's dictionary, 
where the strings in words are sorted lexicographically by the rules of this new language.

Return a string of the unique letters in the new alien language sorted in lexicographically increasing order by the new language's rules. 
If there is no solution, return "". If there are multiple solutions, return any of them.

A string s is lexicographically smaller than a string t if at the first letter where they differ, 
the letter in s comes before the letter in t in the alien language. If the first min(s.length, t.length) letters are the same, 
then s is smaller if and only if s.length < t.length.



Example 1:

Input: words = ["wrt","wrf","er","ett","rftt"]
Output: "wertf"
Example 2:

Input: words = ["z","x"]
Output: "zx"
Example 3:

Input: words = ["z","x","z"]
Output: ""
Explanation: The order is invalid, so return "".
"""


class Solution:
    def alienOrder(self, words):
        # Get all unique_chars
        
        unique_chars, dict1 = set(), {}
        
        for i, word in enumerate(words):
            unique_chars = unique_chars | set(word)
                
        for c in unique_chars:
            dict1[c] = set()
        
        # Build graph
        for i in range(len(words)-1):
            w1, w2 = words[i], words[i+1]
            
            if w1.startswith(w2) and len(w1) > len(w2):
                return ""
            
            for c1,c2 in zip(w1,w2):
                if c1 != c2:
                    dict1[c1].add(c2)
                    break
                    
        # Topological sort
        dict2, stack = defaultdict(int), []
        
        for i in dict1:
            for j in dict1[i]:
                dict2[j] += 1
                
                
        for i in unique_chars:
            if dict2[i] == 0:
                stack.append(i)
                
        visited, res = set(), []
        
        while stack:
            
            node = stack.pop(0)
            
            visited.add(node)
            res.append(node)
            
            for neighbor in dict1[node]:
                dict2[neighbor] -= 1
                
                if dict2[neighbor] == 0:
                    stack.append(neighbor)
        
        return "".join(res) if len(visited) == len(unique_chars) else ""

