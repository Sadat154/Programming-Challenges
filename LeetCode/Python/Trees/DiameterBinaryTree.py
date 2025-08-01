# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.diameter = 0  # Global tracker

        def dfs(node):
            if not node:
                return 0  # Depth of null node is 0

            left = dfs(node.left)
            right = dfs(node.right)

            # Update diameter at this node
            self.diameter = max(self.diameter, left + right)

            # Return depth to parent
            return 1 + max(left, right)

        dfs(root)
        return self.diameter



# Redo this one 