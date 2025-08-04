from typing import List

# Design an algorithm to encode a list of strings to a single string. 
# The encoded string is then decoded back to the original list of strings.
# Please implement encode and decode

# Time complexity: O(n)
# Space complexity: O(n + m) - n = length of the strings, m = number of strings
class Solution1:
    def encode(self, strs: List[str]) -> str:
        encoded = ""    # Initialize an empty string
        for string in strs: # We want to encode every string in the list of strings strs
            encoded += str(len(string)) + "#" + string  # The encoded string will be '<length>#' e.g. hello4#
        
        return encoded  # We return the encoded string e.g. hello4#world4#
    
    def decode(self, s: str) -> List[str]:
        decoded = []    # Initialzie an empty list to store our decoded string/s
        i = 0   # Initialize the counter

        while i < len(s):   # While i is smaller than the length of the string
            j = i   # Initialize a second index pointer j
            while s[j] != '#':  # while the character at index j is not "#"
                j += 1  # We move the index j to the right and keep checking other characters
            
            length = int(s[i:j])    # Length of the string to decode, i is beginning of the string and j is the end. This is for the number we encoded.
            i = j + 1   # We move the first index to the position of the right index + 1
            j = i + length  # The right index becomes the sum of the left index and the length of the encoded string
            decoded.append(s[i:j])  # We append the result to the decoded list with the range of i and j
            i = j   # index i becomes equal to the index j and we restart the loop
        return decoded  # We return the decoded string