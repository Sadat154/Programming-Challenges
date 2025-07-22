# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        self.subRootCheck = []

        def traverseTree(node):
            if not node:
                self.subRootCheck.append('null')  # Mark missing nodes
                return
            self.subRootCheck.append(f'#{node.val}')  # Use # to avoid collision with 'null'
            traverseTree(node.left)
            traverseTree(node.right)

        traverseTree(root)
        x = self.subRootCheck.copy()  # Don't reuse the list
        self.subRootCheck = []
        traverseTree(subRoot)
        y = self.subRootCheck


        # Convert to strings and check if y is a sublist of x
        return ''.join(map(str, y)) in ''.join(map(str, x))
#not optimal, try again later