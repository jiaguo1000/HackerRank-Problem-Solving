class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return(-1)
        
        left = 0
        right = len(nums)-1
        
        if left==right:
            if nums[0]==target:
                return(0)
            if nums[0]!=target:
                return(-1)
        
        while left <= right:
            mid = int(left + (right-left)/2)
            if nums[mid]==target:
                return(mid)
            elif nums[mid] < target:
                left = mid+1
            elif nums[mid] > target:
                right = mid-1
        
        return(-1)