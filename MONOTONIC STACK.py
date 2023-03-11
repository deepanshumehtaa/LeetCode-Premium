"""
Algo: nearest smaller element
1. Online Stock Span
2. Next Greater Element II  (monotonic stack)
3. 739. Daily Temperatures (monotonic stack)
4. Largest Rectangle in Histogram (monotonic stack)
5. Next Greater Node In Linked List
6. Find the Most Competitive Subsequence
7. Sum of Subarray Minimums (previously asked)
8. 1793. Maximum Score of a Good Subarray
Divide Array in Sets of K Consecutive Numbers
Next Greater Element II
Number Of Rectangles That Can Form The Largest Square
Longest Well-Performing Interval


Monotonic Stack
It is a stack data structure in which the elements are sorted in a specific order,
either in increasing or decreasing order.
In a monotonic increasing stack, the elements are sorted in increasing order, [top element being the largest],
while in a monotonic decreasing stack, sorted in decreasing order [top element being the smallest].

Monotonic stack is useful in solving problems that involve:
 finding the nearest greater or smaller element for each element in an array or sequence.

using a monotonic stack, we can efficiently keep track of the elements in the array/sequence that
have not yet found their nearest greater or smaller element.

Ex of problems of monotonic stack:
- finding the largest rectangle in a histogram
- finding the next greater element in an array
- finding the maximum frequency stack.
"""


# 739. Daily Temperatures ..............................................
def dailyTemperatures(T):
  """
  check if it is greater than the temperature at the top of the stack. 
  If it is, we know that all the temperatures in the stack up to the current temperature must be lower than it, 
  so we can pop them off the stack and update their corresponding result values (the number of days until a warmer temperature). 
  We repeat this process until either the stack is empty or the current temperature is not greater than the top of the stack. 
  
  Finally, we add the index of the current temperature to the stack and move on to the next temperature.
  
  """
  stack = []
  res = [0] * len(T)

  for i in range(len(T)):
      while stack and T[i] > T[stack[-1]]:
          idx = stack.pop()
          res[idx] = i - idx
      stack.append(i)

  return res

# Trapping Rain Water ............................................................
def trap(height):
    """
    For each element, we check if the current height is greater than the height of the element at the top of the stack.
    If it is, we pop the elements from the stack until we find an element that is greater than or equal to the current element,
    and calculate the amount of water trapped between the two elements.
    """
    stack = []
    water = 0
    for i in range(len(height)):
        while stack and height[i] > height[stack[-1]]:
            bottom = height[stack.pop()]
            if not stack:
                break
            distance = i - stack[-1] - 1
            depth = min(height[stack[-1]], height[i]) - bottom
            water += distance * depth
        stack.append(i)
    return water


# Remove Duplicate Letters ..........................................................................
def removeDuplicateLetters(s: str) -> str:
    """
    If the character c is not in the stack, 
    remove all chars from the stack that are greater than c and appear later in the input string. 
    
    This is because we want to keep the smallest lexicographical order. 
    We will keep removing characters until either the stack is empty or the top element of the stack is less than or equal to c.
    """
    stack = []
    seen = set()
    last_occurrence = {c: i for i, c in enumerate(s)}

    for i, c in enumerate(s):
        if c not in seen:
            while stack and c < stack[-1] and i < last_occurrence[stack[-1]]:
                seen.remove(stack.pop())
            seen.add(c)
            stack.append(c)

    return "".join(stack)


# Next Greater Element I ...............................................................
def nextGreaterElement(nums1, nums2):
    stack = []
    next_greater = {}
    for num in nums2:
        while stack and stack[-1] < num:
            next_greater[stack.pop()] = num
        stack.append(num)
    while stack:
        next_greater[stack.pop()] = -1
    return [next_greater[num] for num in nums1]


# Example usage:
nums1 = [4, 1, 2]
nums2 = [1, 3, 4, 2]
print(nextGreaterElement(nums1, nums2))


# Largest Rectangle in Histogram
def largestRectangleArea(heights):
    """
    After processing all bars, we pop the remaining elements from the stack and calculate the area of the corresponding rectangles.
    """
    stack = [-1]  # We use a monotonic increasing stack of indices
    max_area = 0

    for i in range(len(heights)):
        while stack[-1] != -1 and heights[stack[-1]] >= heights[i]:
            # Pop elements from the stack until we find an element
            # whose height is less than the height of the current bar.
            # This is because we have found the right boundary of the
            # rectangle corresponding to the popped element.
            height = heights[stack.pop()]
            width = i - stack[-1] - 1
            area = height * width
            max_area = max(max_area, area)

        stack.append(i)

    # After processing all bars, pop the remaining elements from the stack
    # and calculate the area of the corresponding rectangles.
    while stack[-1] != -1:
        height = heights[stack.pop()]
        width = len(heights) - stack[-1] - 1
        area = height * width
        max_area = max(max_area, area)

    return max_area

  
  
# 901. Online Stock Span
# Design an algorithm that collects daily price quotes for some stock and returns the span of that stock's price for the current day
class StockSpanner:

def __init__(self):
    self.stack = []

def next(self, price: int) -> int:
    ans = 1
    while self.stack and self.stack[-1][0] <= price:
        ans += self.stack.pop()[1]

    self.stack.append([price, ans])

    return ans
