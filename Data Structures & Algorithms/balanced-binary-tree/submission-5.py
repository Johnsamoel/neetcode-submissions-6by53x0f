# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        
        left = self.dfs(root.left)
        right = self.dfs(root.right)

        balanced = (abs(left - right) <= 1)
        if not balanced:
            return False
        
        if abs(left - right) > 1:
            return False
        
        return self.isBalanced(root.left) and self.isBalanced(root.right)

    def dfs(self, node: Optional[TreeNode]) -> int:
        if not node:
            return 0

        return 1 + max(self.dfs(node.right), self.dfs(node.left))