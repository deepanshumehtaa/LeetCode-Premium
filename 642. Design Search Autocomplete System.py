"""
642. Design Search Autocomplete System for a search engine. Users may input a sentence (at least one word and end with a special character '#')


Here are the specific rules:

1. The hot degree for a sentence is defined as the number of times a user typed the exactly same sentence before.

2. The returned top 3 hot sentences should be sorted by hot degree (The first is the hottest one). If several sentences have the same hot degree, use ASCII-code order (smaller one appears first).

3. If less than 3 hot sentences exist, return as many as you can.
4. When the input is a special character, it means the sentence ends, and in this case, you need to return an empty list.


eX:

1.
Input
["AutocompleteSystem", "input", "input", "input", "input"]
[[["i love you", "island", "iroman", "i love leetcode"], [5, 3, 2, 2]], ["i"], [" "], ["a"], ["#"]]

Output
[null, ["i love you", "island", "i love leetcode"], ["i love you", "i love leetcode"], [], []]

Explanation:
AutocompleteSystem obj = new AutocompleteSystem(["i love you", "island", "iroman", "i love leetcode"], [5, 3, 2, 2]);
obj.input("i"); // return ["i love you", "island", "i love leetcode"]. There are four sentences that have prefix "i". Among them, "ironman" and "i love leetcode" have same hot degree. Since ' ' has ASCII code 32 and 'r' has ASCII code 114, "i love leetcode" should be in front of "ironman". Also we only need to output top 3 hot sentences, so "ironman" will be ignored.
obj.input(" "); // return ["i love you", "i love leetcode"]. There are only two sentences that have prefix "i ".
obj.input("a"); // return []. There are no sentences that have prefix "i a".
obj.input("#"); // return []. The user finished the input, the sentence "i a" should be saved as a historical sentence in system. And the following input will be counted as a new search.

"""




class AutocompleteSystem:
    """
    Key ideas:

    Store all sentences with their frequency (times) as tuples in a trie (use "SKEY" to mark sentences)
    Each node in a trie is also a sub(trie) (similar to the concept of each tree being a subtree)
    As the user inputs more characters, we go deeper into our trie, i.e we keep track of the current user input (a string) and its correlating subtrie
    All sentences that can be formed with the current user input as prefix can thus be found via DFS through our current subtrie
    Upon request, find the top 3 candidates and sort them
    """


    def __init__(self, sentences: List[str], times: List[int]):
        self.root_trie = {}
        self.curr_trie = self.root_trie
        self.curr_input = ""
        self.SKEY = "%%%"
        n = len(sentences)
        for i in range(n):
            current = self.root_trie 
            for s in sentences[i]:
                current = current.setdefault(s, {})
            current[self.SKEY] = (times[i], sentences[i])

    def findSentencesDFS(self, trie):
        res = []
        if self.SKEY in trie:
            res.append(trie[self.SKEY])
        for key, value in trie.items():
            if key != self.SKEY:
                res += self.findSentencesDFS(value)
        return res
            
    def input(self, c: str) -> List[str]:
        # Add current input as a sentence and update it's frequency
        if c == '#':
            if self.SKEY in self.curr_trie:
                self.curr_trie[self.SKEY] = (self.curr_trie[self.SKEY][0]+1, self.curr_trie[self.SKEY][1])
            else:
                self.curr_trie[self.SKEY] = (1, self.curr_input)
			# Reset trie and input state
            self.curr_input = ""
            self.curr_trie = self.root_trie
        
        # Add c to current input and go deeper into trie
        else:
            self.curr_input += c
            if c not in self.curr_trie: 
                self.curr_trie = self.curr_trie.setdefault(c, {})
            else:
                self.curr_trie = self.curr_trie[c]            
                candidates = self.findSentencesDFS(self.curr_trie)
                topK = min(3, len(candidates))
                return [x[1] for x in sorted(candidates, key=lambda x: (-x[0], x[1]))[:topK]]
            
        
        return []
    
"""
Trie + hEAP
"""

class AutocompleteSystem:
	def __init__(self, sentences: List[str], times: List[int]):
		self.root = {}
		for sentence, count in zip(sentences, times):
			self.register(sentence, count)
		self.curr_input = []
		self.curr_node = self.root

	def register(self, sentence, count):
		node = self.root
		for char in sentence:
			node = node.setdefault(char, {"cnt":{}})
			node["cnt"][sentence] = node["cnt"].get(sentence, 0) + count

	def input(self, c: str) -> List[str]:
		if c == "#":
			self.register(''.join(self.curr_input), 1)
			self.curr_input = []
			self.curr_node = self.root
			return []
		else:
			self.curr_input.append(c) 
			if self.curr_node and c in self.curr_node:
				self.curr_node = self.curr_node[c]
				heap = [(-count, sentence) for sentence,count in self.curr_node["cnt"].items()]
				return [res[1] for res in heapq.nsmallest(3, heap)]
			else:
				self.curr_node = None
				return []


