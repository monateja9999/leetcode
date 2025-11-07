#Learning Python

import sys
print(sys.version)

# Lists (Stacks)
l = []               # empty list
l = [1, 2, 3]        # with elements
l = list(range(5))   # [0, 1, 2, 3, 4]


l.append(5)
l.extend([6,5,5])
l.pop()
l.remove(5)
l.insert(2, 7)
# l.sort()
# l.sort(reverse = True)
l.reverse()
print(l)

l2 = sorted(l, reverse = True)
print(l2)
print(sum(l))
print(max(l))
print(min(l))
print(any(l))
print(all(l))
l.remove(0)
print(all(l))
l3 = [x for x in l if x >= 2]
print(l3)


# Queues

from collections import deque

q = deque(l)
print(q)

q.append(11)
q.appendleft(12)
q.pop()
q.popleft()
print(q)

q.remove(6)

q.extendleft(l)
q.extend([11,12])
print(q)
# q.clear()
print(q)
if q: print(len(q))


# Matrices


matrix = [[0]*5 for i in range(5)]
print(matrix)

import numpy as np

mat2 = np.zeros((2,3))
mat2[1][2] = 8
print(mat2)
mat2 = mat2.astype(int)
print(mat2)

mat3 = np.ones((2,3), dtype = int)
print(mat3)

mat2 = mat2.T
print(mat2)

mat4 = np.dot(mat3, mat2)

print("Matrix 4:\n",mat4)

print(4*mat4[1][1])


matrix = [[0]*4]*4
print("\nMatrix:\n")

matrix[0][0] = 1

print(matrix)

matrix2 = [[0]*4 for i in range(4)]

matrix2[0][0] = 1

print(matrix2)


# Disctionaries or Hashmaps

d = {}
d = {'a' : 20, 'b': 30}
d2 = dict(e = 40, f = 50)
print(d)
print(d2)
# d3 = d2 + d
# print(d3)

from collections import defaultdict, Counter

# defaultdict to handle missing keys automatically
counts = defaultdict(int)
counts['apple'] += 1

string = "abcde"
string2 = "fefghi"
c1 = Counter(string)
c2 = Counter(string2)
c3 = c1+c2

for key, value in c1.items():
	print(key, value)
print(c3)
finaldict = sorted(c3.items(), key=lambda x:(x[1], x[0]), reverse = True)
print(finaldict)


del c2['f']

print(c2)


from collections import OrderedDict

od = OrderedDict()
od['second'] = 1
od['first'] = 2
od['third'] = 2

print(od)

od.popitem(last = False)
print(od)
od['fourth'] = 3
print(od)
od.move_to_end('third')
print(od)
od.move_to_end('third', last=False)
print(od)



from sortedcontainers import SortedDict

sd = SortedDict()

sd['b'] = 1
sd['c'] = 2
sd['a'] = 3

print(sd)


for key in sd.irange('a','b'):
	print(key, value)


#Sets

s = set()
s2 = {1,2,3}
s.add(11)
s.add(12)
s.add(13)
print(s)
s.pop()
s.pop()
print(s)
print(s2)
s2.discard(4) # Safe Removal
print(s)


set1 = {1,2,3,4,5}
set2 = {3,4,5,6,7}

union = set1.union(set2)
print(union)
intersection = set1.intersection(set2)
difference = set1.difference(set2)
difference2 = set2.difference(set1)
print(intersection)
print(difference)
print(difference2)


l = [1,1,1,1,2,3,3,4,2,5]
s = set(l)
print(s)

from sortedcontainers import SortedSet

s = SortedSet([1, 3, 5, 7, 9])
for x in list(s.irange(2, 8)):
    s.discard(x)

print(s)

# HEAPS

import heapq

nums = [5, 1, 3, 7]
heapq.heapify(nums)        # in-place min-heap
heapq.heappush(nums, 0)    # push new element
smallest = heapq.heappop(nums)

kthsmallest = heapq.nsmallest(1,nums)
print(nums)
print(kthsmallest)

nums = [-x for x in nums]
heapq.heapify(nums)
max_val = -heapq.heappop(nums)

print(max_val)


import bisect

arr = [1, 3, 4, 7]
bisect.insort(arr, 5)      # inserts while keeping sorted
idx = bisect.bisect_left(arr, 4)   # find insertion index
idx2 = bisect.bisect_right(arr, 4)   # find insertion index

print(idx, idx2)

from sortedcontainers import SortedList

sl = SortedList([4, 1, 3])
sl.add(2)
print(sl)       # SortedList([1, 2, 3, 4])
sl.discard(3)
sl.bisect_left(2)


import itertools as it

# combinations
print("combinations([1,2,3], 2):", list(it.combinations([1,2,3], 2)))
# Output: [(1, 2), (1, 3), (2, 3)]

# permutations
print("permutations([1,2,3]):", list(it.permutations([1,2,3])))
# Output: [(1, 2, 3), (1, 3, 2), (2, 1, 3), (2, 3, 1), (3, 1, 2), (3, 2, 1)]

# product
print("product([1,2], [3,4]):", list(it.product([1,2], [3,4])))
# Output: [(1, 3), (1, 4), (2, 3), (2, 4)]

# accumulate
print("accumulate([1,2,3,4]):", list(it.accumulate([1,2,3,4])))
# Output: [1, 3, 6, 10]

# chain multiple lists
print("chain([1,2], [3,4]):", list(it.chain([1,2], [3,4])))
# Output: [1, 2, 3, 4]

# groupby
print("groupby('aaabbc'):")
for k, g in it.groupby('aaabbc'):
    print(k, list(g))
# Output:
# a ['a', 'a', 'a']
# b ['b', 'b']
# c ['c']



for i, val in enumerate(['a', 'b', 'c']):
    print(i, val)


names = ['Alice', 'Bob']
scores = [85, 90]
for name, score in zip(names, scores):
    print(name, score)


nums = [1, 2, 3, 4]

# -------------------------
# 1️⃣ map()
# Applies a function to each element of an iterable and returns an iterator
squares = list(map(lambda x: x**2, nums))
print("Squares:", squares)
# Output: [1, 4, 9, 16]
# Explanation: 1**2=1, 2**2=4, 3**2=9, 4**2=16

# -------------------------
# 2️⃣ filter()
# Keeps only the elements where the function returns True
evens = list(filter(lambda x: x % 2 == 0, nums))
print("Even numbers:", evens)
# Output: [2, 4]
# Explanation: 2%2==0 and 4%2==0 → keep these, discard others

# -------------------------
# 3️⃣ reduce()
# Applies a binary function cumulatively to the elements
from functools import reduce
total = reduce(lambda a, b: a + b, nums)
print("Sum:", total)
# Output: 10
# Explanation: ((1+2)+3)+4 = 10

# Another example with reduce: product of all elements
product = reduce(lambda a, b: a * b, nums)
print("Product:", product)
# Output: 24
# Explanation: ((1*2)*3)*4 = 24



# Sum of squares of even numbers
sum_even_squares = reduce(lambda a, b: a + b, map(lambda x: x**2, filter(lambda x: x%2==0, nums)))
print("Sum of squares of evens:", sum_even_squares)
# Output: 2**2 + 4**2 = 4 + 16 = 20
from collections import Counter

c = Counter("banana")
print(c.most_common(2))  # [('a', 3), ('n', 2)]

def bisect_left (list: nums, int: target) -> int:
    left, right = 0, len(nums)
    while left < right:
        mid = (left + right) // 2
        if nums[mid] <= target:
            left = mid + 1
        else:
            right = mid
    return left

def bisect_right(list: nums, int: target) -> int:
    left, right = 0, len(nums)
    while left < right:
        mid = (left + right) // 2
        if nums[mid] <= target:
            left = mid + 1
        else:
            right = mid
    return left

