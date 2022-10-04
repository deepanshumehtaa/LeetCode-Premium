"""
You are given an array of strings products and a string searchWord.

Design a system that suggests at most three product names from products after each character of searchWord is typed. 
Suggested products should have common prefix with searchWord. 
If there are more than three products with a common prefix return the three lexicographically minimums products.

Return a list of lists of the suggested products after each character of searchWord is typed.



Ex:
Input: products = ["mobile","mouse","moneypot","monitor","mousepad"], searchWord = "mouse"

Output: [["mobile","moneypot","monitor"],["mobile","moneypot","monitor"],["mouse","mousepad"],["mouse","mousepad"],["mouse","mousepad"]]

Explanation: products sorted lexicographically = ["mobile","moneypot","monitor","mouse","mousepad"].
After typing m and mo all products match and we show user ["mobile","moneypot","monitor"].
After typing mou, mous and mouse the system suggests ["mouse","mousepad"].
"""



class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        
        class TrieNode(object):
            def __init__(self):
                self.children = defaultdict(TrieNode)
                self.sugguestions = []
                
            def add_suggestion(self, word):
                self.sugguestions.append(word)
        
        trie = TrieNode()
        for product in sorted(products):
            root = trie
            for c in product:
                root = root.children[c]
                root.add_suggestion(product)
        
        result, root = [], trie
        for c in searchWord:
            root = root.children[c]
            result.append(root.sugguestions[:3])
        return result
