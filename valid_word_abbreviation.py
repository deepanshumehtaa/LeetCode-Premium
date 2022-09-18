"""
Valid Word Abbreviation: https://leetcode.com/problems/valid-word-abbreviation/

"""
import sys

d1 = {}
d2 = set()
d3 = []
d4 = ()

print(sys.getsizeof(d1))  # empty dict contains 64 byte i.e. 2^6
print(sys.getsizeof(d2))  # empty set contains 216 byte
print(sys.getsizeof(d3))  # empty list contains 56 byte
print(sys.getsizeof(d4))  # empty tuple contains 40 bytes

d4_4 = (1, 2, 3, 4, 5, "6")
print(sys.getsizeof(d4_4))  # tuple with 5 int contains 80 bytes (8 byte/num)
print(sys.getsizeof(list(d4_4)))  # list with 5 int contains 96 bytes



