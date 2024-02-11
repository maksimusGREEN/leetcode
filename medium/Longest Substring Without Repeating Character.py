# Given a string s, find the length of the longest substring without repeating characters.


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        d = {}
        i, j = 0, 0
        ans = 0

        while j<=len(s)-1:

            if s[j] in d:
                i = max(d[s[j]]+1, i)
                
            d[s[j]] = j
            ans = max(j-i+1, ans)
            j+=1
        
        return ans
    
print(Solution().lengthOfLongestSubstring('abba'))