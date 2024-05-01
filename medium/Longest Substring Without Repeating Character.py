# Given a string s, find the length of the longest substring without repeating characters.


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        d = {}
        i, j = 0, 0
        ans = 0

        while j<len(s):

            if s[j] in d:
                i = max(d[s[j]]+1, i)
                
            d[s[j]] = j
            ans = max(j-i+1, ans)
            j+=1
        
        return ans
    
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        lp, rp = 0, 0
        hash_set = set()
        ans=0
        
        while rp<len(s):
            if s[rp] not in hash_set:
                hash_set.add(s[rp])
                ans = max(ans, rp-lp+1)
                rp+=1
            else:
                if s[lp] in hash_set:
                    hash_set.remove(s[lp])
                lp+=1
        return ans
    
print(Solution().lengthOfLongestSubstring('abba'))