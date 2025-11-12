class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        prices = [float("inf")] * n
        prices[src] = 0
        stops = 0
        while stops < k + 1:
            temp_prices = prices.copy()
            for s,d,p in flights:
                if prices[s] == float("inf"):
                    continue
                temp_prices[d] = min(temp_prices[d], prices[s] + p)
            prices = temp_prices
            stops += 1
        return prices[dst] if prices[dst] != float("inf") else -1 


1) 
You are given a 1-D array.
e.g. [2 , 3,| 1, 5,| 4] (k, x) = (3, 3), (3, 5)

Cut this array into k sub arrays.
Write a function to return:

True if min(sum(each sub array)) >= x
False otherwise

k > 0


Class Solution:
  def subarray_min(self, k: int, x: int, arr: list)-> bool: 
    if not arr:
      return False
    pre_sum = 0
    for i in range(len(arr)): 
      pre_sum += arr[i] i = 4 --> e: 1 # arr[5]
      if pre_sum >= x:
        k -= 1
        pre_sum = 0
      if k == 0:
        return True
    return False
   
TC O(n), SC O(1)

2) You are given a 1-D array.
  [2 , 3, 1, 5, 4] k=3 --> 2 | 3 | 1,5,4 = 10
  answer < 
min_val = 1
  0 < k < len(arr)
  2 | 3 | 1,5,4 --> 2 | 3| 10 --> 2
  2, 3| 1| 5, 4 --> 1
  2, 3,| 1, 5,| 4 --> 4 (answer)
Cut this array into k sub arrays.
Write a function to return 
  the maximized minimum sum among different sub arrays.

  
[] = n elements
1 <= k <= n

min_val = min(arr) 
[2 , 3,| 1, | 5, 4] 
k = k - 1


  
  
k > 0
all are positive numbers

Class Solution:
  def subarray_min(self, k: int, arr: list)-> bool: 
    if not arr:
      return False
    pre_sum = 0
    max_sum = 0
    for i in range(len(arr)): 
      pre_sum += arr[i] i = 4 --> e: 1 # arr[5]
      if pre_sum >= x:
        k -= 1
        max_sum = max(max_sum, pre_sum)
        last_idx = i
        pre_sum = 0
      if k == 0:
        return True
    return False