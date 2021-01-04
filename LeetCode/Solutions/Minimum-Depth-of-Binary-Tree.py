# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return(0)
        
        q = []
        visited = []
        level = [1]
        
        q.append(root)
        visited.append(root)
        
        while q:
            curr = q.pop(0)
            curr_level = level.pop(0)
            if (not curr.left) and (not curr.right):
                return(curr_level)
            
            for child in [curr.left, curr.right]:
                if child and (child not in visited):
                    q.append(child)
                    visited.append(child)
                    level.append(curr_level+1)