class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        
        m = len(nums1)
        n = len(nums2)
        final_list = []
        # i = j = 0
        if ((m+n) % 2) == 0:
            final_len = (m+n)/2 + 1
        else:
            final_len = (m+n)//2 + 1
            
        while nums1 and nums2 and len(final_list)<final_len:
            if nums1[0] < nums2[0]:
                final_list.append(nums1[0])
                nums1.pop(0) 
            else:
                final_list.append(nums2[0])
                nums2.pop(0) 
        
        if nums1 and len(final_list)<final_len:
            final_list = final_list + nums1[:int(final_len-len(final_list))]
        if nums2 and len(final_list)<final_len:
            final_list = final_list + nums2[:int(final_len-len(final_list))]  
        
        print(final_list)
        if ((m+n) % 2) == 0:
            return(mean(final_list[-2:]))
        else:
            return(final_list[-1])
            