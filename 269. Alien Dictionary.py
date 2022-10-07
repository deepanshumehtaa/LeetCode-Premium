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
        """Python BFS"""

        indegree = {key: 0 for key in ''.join(words)}
        adjList = collections.defaultdict(list)

        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i + 1]
            minLen = min(len(w1), len(w2))
            if len(w1) > len(w2) and w1[:minLen] == w2[:minLen]:
                return ""
            for j in range(minLen):
                if w1[j] != w2[j]:
                    adjList[w1[j]].append(w2[j])                    
                    indegree[w2[j]] += 1                        
                    break

        queue = collections.deque([k for k in indegree if indegree[k] == 0])

        result = []
        while queue:
            letter = queue.popleft()
            result.append(letter)
            for neighbor in adjList[letter]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    queue.append(neighbor)
        return ''.join(result) if len(result) == len(indegree) else ''

    
# ........................................................................................................
"""

build the list
words = ["wrt","wrf","er","ett","rftt"]
first_word: wrt, second_word: wrf
do not add w == w
do not add r == r
do not add t == f
add t---> f
first_word: wrf, second_word: er
do not add w == e
add w---> e
first_word: er, second_word: ett
do not add e == e
do not add r == t
add r---> t
first_word: ett, second_word: rftt
do not add e == r
add e---> r
{'w': [], 'r': ['e'], 't': ['r'], 'f': ['t'], 'e': ['w']}

"""

class Solution:
    def alienOrder(self, words: List[str]) -> str:
        # build the list
        adj_list = {c : [] for word in words for c in word}
           # Step 1: Find all edges and put them in adj_list.
        for first_word, second_word in zip(words, words[1:]):
            for c, d in zip(first_word, second_word):
                if c != d: 
                    adj_list[d].append(c)
                    break
            else: # Check that second word isn't a prefix of first word.
                if len(second_word) < len(first_word): 
                    return ""
        
        
        seen , cycle = set(),set()
        output = []
        def dfs(node): 
            if node in cycle:
                return False
            if node in seen: # no issue no need to visit again , we visit node more then once
                return True
            
            cycle.add(node)
            for per in adj_list[node]:
                if dfs(per) == False: # return result 
                    return False
            cycle.remove(node)
            seen.add(node)
            output.append(node)
                
        
        for c in adj_list:
            if dfs(c) == False: # found a cycle 
                return ""
        return "".join(output)
    
 # ......................................................................................

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

