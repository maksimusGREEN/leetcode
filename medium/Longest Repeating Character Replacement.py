# You are given a string s and an integer k. 
# You can choose any character of the string and change it to any other uppercase English character.
# You can perform this operation at most k times.

# Return the length of the longest substring containing the same letter you can get after performing the above operations.


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        dic_freq = {}
        max_len = 0
        max_count = 0

        for right in range(len(s)):
            dic_freq[s[right]] = dic_freq.get(s[right], 0)+1
            max_count = max(max_count, dic_freq[s[right]])
            
            if right-left+1-max_count > k:
                dic_freq[s[left]] -=1
                left+=1
            max_len = max(max_len, right-left+1)
        
        return max_len