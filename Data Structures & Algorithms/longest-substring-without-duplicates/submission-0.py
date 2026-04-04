class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        sett = set()
        l = 0
        longest = 0
        
        for r in range(len(s)):
            # While the current character is a duplicate:
            # 1. Remove the leftmost character from the set
            # 2. Move the left pointer forward
            while s[r] in sett:
                sett.remove(s[l])
                l += 1
            
            sett.add(s[r])
            
            longest = max(longest, r - l + 1)
            
        return longest