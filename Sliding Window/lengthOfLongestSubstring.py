# Given a string s, find the length of the longest substring without duplicate characters.
# A substring is a contiguous sequence of characters within a string.

# Time complexity: O(n)
# Space complexity: O(n)
class Solution1:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet = set()
        result = 0
        left = 0

        for right in range(len(s)):
            while s[right] in charSet:
                charSet.remove(s[left])
                left += 1
            charSet.add(s[right])
            result = max(result, right - left + 1)
        return result

# Time complexity: O(n * m) - n is the length of the string, m is the total number of unique characters in the string
# Space complexity: O(m)
class Solution2:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        for i in range(len(s)):
            charSet = set()
            for j in range(i, len(s)):
                if s[j] in charSet:
                    break
                charSet.add(s[j])
            res = max(res, len(charSet))
        return res

# Time complexity: O(n) - n is the length of the string
# Space complexity: O(m) - m is the total number of unqiue characters in the string
class Solution3:
    def lengthOfLongestSubstring(self, s: str) -> int:
        map = {}
        left = 0
        result = 0

        for right in range(len(s)):
            if s[right] in map:
                left = max(map[s[right]] + 1, left)
            map[s[right]] = right
            result = max(result, right - left + 1)
        return result