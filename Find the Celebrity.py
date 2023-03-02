"""
This problem can be solved with:
- Array
- Two Pointers
- Stack
- Greedy
- Graph
- Divide and Conquer
"""

# knows is the API already defined by LeetCode which tells
# whether `a knows b`

# just patching the api
def knows(a:int, b:int):
    # only api knows the relation b/w a & b index
    return True


class Solution:
    """
    Q: [[1,0,1],[1,1,0],[0,1,1]]
    A: -1
    How?
    [
        [1,0,1], --> [<knows himself>, <dont know 2nd person>, <know 3rd person>]
        [1,1,0], --> [<knows 1st person>, <knows himself>, <don't know 3rd person>]
        [0,1,1], --> [<dont know 2nd person>, <knows himself>, <know 3rd person>]
     ]

    Best solved with stack_sol
    """

    def my_friend_solution(self, n: int) -> int:
        """
        first for loop for finding who might be the possible candidate who can be celebrity.
        After there we get to know who can be the celebrity

        ex: [[1,1,0],[0,1,0],[1,1,1]] for this, we get the possible celeb as from the for loop we get 1 after that, for the second fop loop we get whether out possible candidate is correct or not
if(knows(possible_celeb,i) or not knows(i,possible_celeb)):
return -1
does that part.

        its just a way of method of elimination, in the first loop we eliminate all the other candidates and keep only one possible celeb
and then we check whether the possible celeb is correct or not.
        """
        possible_celeb = 0
        for i in range(1, n):
            if (knows(possible_celeb, i)):
                possible_celeb = i
        # print(possible_celeb)
        for i in range(n):
            if (i == possible_celeb):
                continue
            else:
                if (knows(possible_celeb, i)):
                    return -1
                if (not knows(i, possible_celeb)):
                    return -1
        return possible_celeb


def findCelebrity(self, n: int) -> int:
    return self.stack_sol(n)
    # return self.linear_time_sol(n)
    # return self.set_solution(n)

def stack_sol(self, n) -> int:
    """BEST"""
    stack = list(range(n))

    while (len(stack) >= 2):
        p1, p2 = stack.pop(), stack.pop()

        if knows(p1, p2):
            stack.append(p2)
        else:
            stack.append(p1)

    celebrity = stack.pop()

    for i in range(n):
        if i != celebrity or (knows(i, celebrity) is False or knows(celebrity, i) is True):
            return -1

    return candidate


def linear_time_sol(self, n):
    # assuming 0th is celeb
    celeb = 0
    for i in range(1, n):
        if knows(celeb, i) is True:
            celeb = i

    for i in range(n):
        if i != celeb:
            if knows(i, celeb) is False or knows(celeb, i) is True:
                return -1

    return celeb


def set_solution(self, n):
    candidates = {i for i in range(n)}  # set, why add & remove by element is faster
    while len(candidates) > 1:
        iterator = iter(candidates)  #
        a = next(iterator)
        b = next(iterator)
        if knows(a, b):
            candidates.remove(a)
        else:
            candidates.remove(b)
    c = next(iter(candidates))

    # check if everyone knows c
    for i in range(n):
        if i == c:
            continue
        if knows(i, c) is False:
            return -1

    # check if c does not know anyone else
    for i in range(n):
        if c == i:
            continue
        if knows(c, i) is True:
            return -1
    return c

