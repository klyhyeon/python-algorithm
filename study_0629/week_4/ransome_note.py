# https://leetcode.com/problems/ransom-note/description/
# Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the letters from magazine and false otherwise.
# Each letter in magazine can only be used once in ransomNote.
# Example 1:
# Input: ransomNote = "a", magazine = "b"
# Output: false
# Example 2:
# Input: ransomNote = "aa", magazine = "ab"
# Output: false
# Example 3:
# Input: ransomNote = "aa", magazine = "aab"
# Output: true
# Constraints:
# 1 <= ransomNote.length, magazine.length <= 10^5
# ransomNote and magazine consist of lowercase English letters.
# 성공: 15분

from collections import defaultdict

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ransom_map = dict()
        for alphabet in ransomNote:
            if alphabet in ransom_map:
                ransom_map[alphabet] += 1
            else:
                ransom_map[alphabet] = 1
        magazine_map = dict()
        for alphabet in magazine:
            if alphabet in magazine_map:
                magazine_map[alphabet] += 1
            else:
                magazine_map[alphabet] = 1
        for key in ransom_map:
            if magazine_map.get(key, 0) < ransom_map.get(key):
                return False
        return True
        

sol = Solution()
print(sol.canConstruct("aa", "aab"))