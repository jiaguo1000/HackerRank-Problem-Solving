class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        dict_nums_idx = {}
        
        for i,second_val in enumerate(nums):
            first_val_temp = target - second_val
            
            if first_val_temp in dict_nums_idx:
                return([dict_nums_idx[first_val_temp], i])
            else:
                dict_nums_idx[second_val] = i