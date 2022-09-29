"""
1166. Design File System


You are asked to design a file system that allows you to create new paths and associate them with different values.

The format of a path is one or more concatenated strings of the form: / followed by one or more lowercase English letters. For example, "/leetcode" and "/leetcode/problems" are valid paths while an empty string "" and "/" are not.

Implement the FileSystem class:

- bool createPath(string path, int value) Creates a new path and associates a value to it if possible and returns true. Returns false if the path already exists or its parent path doesn't exist.
- int get(string path) Returns the value associated with path or returns -1 if the path doesn't exist.

Input: 
["FileSystem","createPath","get"]
[[],["/a",1],["/a"]]
Output: 
[null,true,1]
Explanation: 
FileSystem fileSystem = new FileSystem();

fileSystem.createPath("/a", 1); // return true
fileSystem.get("/a"); // return 1


Input: 
["FileSystem","createPath","createPath","get","createPath","get"]
[[],["/leet",1],["/leet/code",2],["/leet/code"],["/c/d",1],["/c"]]
Output: 
[null,true,true,2,false,-1]
Explanation: 
FileSystem fileSystem = new FileSystem();

fileSystem.createPath("/leet", 1); // return true
fileSystem.createPath("/leet/code", 2); // return true
fileSystem.get("/leet/code"); // return 2
fileSystem.createPath("/c/d", 1); // return false because the parent path "/c" doesn't exist.
fileSystem.get("/c"); // return -1 because this path doesn't exist.
"""

"""
Solutions Sugested by LeetCode:
1.  Dictionary for storing paths
2.  Trie based approach (https://leetcode.com/problems/design-file-system/Figures/1166/img2.png)

1.  Dictionary for storing paths:
    Simulation-based approach because it doesn't use any fancy data-structure for storing the paths and pretty much, we do what the problem asks us to do for both the functions. We simply need a key-value data structure with some additional processing to verify the validity of a path being added. Naturally, a HashMap or a dictionary seems to be a good data structure to go with.

Algorithm

Initialize a dictionary or a HashMap called paths that will have the key as the path input to our create function and the value would be the value passed to the function.

For our create function, we have three steps that we need to do:

Step-1 is that we do a basic verification of the path being valid or not. Here we check if the path is empty, or "/" or if the path already exists in our dictionary. If any of these conditions are met, we simply return false.
The second step is to obtain the parent path of the provided path and check its presence in the dictionary. If the parent path doesn't exist, then we simply return false. Else, we move on.
Note that checking for just the parent is enough because the presence of the parent path ensures that the grandparent (and other ancestors by this logic) would also exist in the dictionary.

Finally, we insert the provided path and value into the dictionary and return true.
For the get function, we simply return a default value of -1 if the path doesn't exist inside the dictionary. Else, we return the actual value.

"""
class Tree:
    def __init__(self, val=None, childredn = defaultdict()):
        
        self.children = {}
        self.val = val
        
class FileSystem:
    """Trie Based Solution"""

    def __init__(self):
        self.root = Tree()
        
    def createPath(self, path: str, value: int) -> bool:
        node = self.root
        if path == "" or path == "/":
            return False 
        paths = path.split('/')
        paths = paths[1:]
        i = 0
        while i < len(paths)-1:
            if paths[i] not in node.children:
                return False
            node = node.children[paths[i]]
            i+=1
        if paths[i] in node.children: 
            return False
        else:
            node.children[paths[i]] = Tree(value)
            
        return True

    def get(self, path: str) -> int:
        node = self.root
        paths = path.split('/')
        paths = paths[1:]
        for path in paths:
            if path not in node.children:
                return -1
            node = node.children[path]
        return node.val


# Your FileSystem object will be instantiated and called as such:
# obj = FileSystem()
# param_1 = obj.createPath(path,value)
# param_2 = obj.get(path)
