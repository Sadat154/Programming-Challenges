# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.isBalanced = True

        def heightCheck(node):
            if not node:
                return 0
            left = heightCheck(node.left)
            right = heightCheck(node.right)

            heightDif = abs(left - right)
            print(heightDif)
            if abs(heightDif) > 1:
                self.isBalanced = False

            return 1 + max(left, right)

        heightCheck(root)

        return self.isBalanced






