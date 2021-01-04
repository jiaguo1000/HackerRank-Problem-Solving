class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        single_res = []
        
        self.DFS(nums, single_res, res)
        return(res)
    
    def DFS(self, nums, single_res, res):
        if not nums:
            res.append(single_res)
            return
        
        for i in range(len(nums)):
            self.DFS(nums[:i]+nums[i+1:], single_res+[nums[i]], res)