class Solution:
    def characterReplacement(self, s, k):
        dict_ch_count = {}
        start_i = res = 0
        max_count_in_window = 0
        
        for end_i in range(len(s)):
            ch = s[end_i]
            dict_ch_count[ch] = dict_ch_count.get(ch, 0) + 1 
            max_count_in_window = max(max_count_in_window, dict_ch_count[ch])
            
            if end_i - start_i + 1 - max_count_in_window > k:
                dict_ch_count[s[start_i]] -= 1 
                start_i += 1
            
            res = max(res, end_i - start_i + 1)
        
        return res