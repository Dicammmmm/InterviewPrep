from collections import Counter

# Given two strings s and t, return true if t is an anagram of s, and false otherwise.

# Time complexity: O(n log n)
# Space complexity: O(n)
class Solution1: 
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):    # If the length is different, they can't be an Anagram. Early exit.
            return False
        
        return sorted(s) == sorted(t)  # If they are an anagram, the  sorted values will be the same. Return True.

# Time complexity: O(n)
# Space complexity: O(k) - k = number of unique characters
class Solution2:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):    # If the length is different, they can't be an Anagram. Early exit.
            return False

        countS, countT = {}, {} # Initialize the hash map (dictionaries)
        
        for i in range(len(s)): # For every index in the range of the length of the string

            # Count of the character s/t at the index of i will be 1 + the count of the character s/t at the index i 
            # and if the character does not exist at the key return 0.
            countS[s[i]] = 1 + countS.get(s[i], 0)  
            countT[t[i]] = 1 + countT.get(t[i], 0)

        return countS == countT # Check if the two hash maps are equal

# Time complexity: O(n)
# Space complexity: O(k) - k = number of unique characters
class Solution3:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):    # If the length is different, they can't be an Anagram. Early exit.
            return False
        
        return Counter(s) == Counter(t) # Does what Solution2 does but shorter