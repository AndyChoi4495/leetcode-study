# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        def dfs(root):
            if not root:
                return 0
            
            right = dfs(root.right)
            left = dfs(root.left)

            if left is False or right is False or abs(left - right) > 1:
                return False
            
            return 1 + max(left,right)
        
        return dfs(root) is not False