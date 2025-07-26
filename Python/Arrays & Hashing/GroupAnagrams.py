from typing import List
from collections import defaultdict

# Given an array of strings strs, group all anagrams together into sublists. You may return the output in any order.
# An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.

# Time complexity: O(m * n log n) - m = number of string, n = length of the longest string
# Space complexity: O(m * n) - m = number of string, n = length of the longest string
class Solution1:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        map = defaultdict(list) # defaultdict(list) creates an empty list for each new key

        for s in strs:                      # For each string in the list
            sortedS = ''.join(sorted(s))    # Sort the letters in the string
            map[sortedS].append(s)          # Append the string to the list in the key
        
        return list(map.values())           # Return the list of values

# Time complexity: O(m * n)
# Space complexity: O(m * n)
class Solution2:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        map = defaultdict(list)                 # defaultdict(list) create an empty list for each new key

        for s in strs:                          # For each string in the list strs
            count = [0] * 26                    # Create an array of 26 0s
            for c in s:                         # For character in the string
                count[ord(c) - ord("a")] += 1   # Convert char to index (a=0, b=1, etc.) and increment count

            map[tuple(count)].append(s)         # Use count pattern as key, append original string to its group
      
        return list(map.values())               # Print the grouped values