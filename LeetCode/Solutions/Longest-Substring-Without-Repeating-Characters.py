class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        dict_ch_idx = {}
        max_so_far = curr_max = start = 0
        
        for i, ch in enumerate(s):
            
            if ch in dict_ch_idx and dict_ch_idx[ch] >= start:
                max_so_far = max(max_so_far, curr_max)
                curr_max = i - dict_ch_idx[ch]
                start = dict_ch_idx[ch] + 1
            else:
                curr_max = curr_max + 1
                
            dict_ch_idx[ch] = i
            
        return max(max_so_far, curr_max)
    