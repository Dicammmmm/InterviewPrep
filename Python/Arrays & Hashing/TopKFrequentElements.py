import heapq
from typing import List

# Given an integer array nums and an integer k, return the k most frequent elements within the array.
# The test cases are generated such that the answer is always unique.
# You may return the output in any order.

# Time complexity: O(n log n) - n = length of the array
class Solution1:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}                              # Empty hashmap for the count of how many times each number appears
        for num in nums:                        # For each number in the list of numbers
            count[num] = 1 + count.get(num, 0)  # The key will be number from the list and the value will be how many times the number appears in the list, default 0

        arr = []                        # Empty array (list) to store [frequency, number] pairs
        for num, cnt in count.items():  # For each number and its frequency in the count map
            arr.append([cnt, num])      # Create [frequency, number] pairs for sorting
        arr.sort()                      # Sort the array in ascending order by frequency

        res = []                        # Empty array for the result
        while len(res) < k:             # While we haven't collected k elements yet
            res.append(arr.pop()[1])    # Pop highest frequency pair and extract the number
        return res

# Time complexity: O(n log k)
# Space complexity: O(n + k)
class Solution2:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}  # Empty hashmap to store the count of how many times each number appears

        for num in nums:    # For each number (key) in the list of numbers add how many times the number appears (value)
            count[num] = 1 + count.get(num, 0)

        heap = []   # Initialize an empty Heap
        for num in count.keys():    # For every number (key) in the count HashMap create a heap with the 
            heapq.heappush(heap, (count[num], num))
            if len(heap) > k:
                heapq.heappop(heap)

        res = []
        for i in range(k):  
            res.append(heapq.heappop(heap)[1])

        return res

# Time complexity: O(n)
# Space complexity: O(n)
class Solution3:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq = [[] for i in range(len(nums) + 1)]

        for num in nums:
            count[num] = 1 + count.get(num, 0)
        for num, cnt in count.items():
            freq[cnt].append(num)
        
        res = []
        for i in range(len(freq) - 1, 0, -1):
            for num in freq[i]:
                res.append(num)
                if len(res) == k:
                    return res

        raise ValueError()