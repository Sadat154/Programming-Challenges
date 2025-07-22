# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        self.ancestor = root

        def check(node):

            if node.val < p.val and node.val < q.val:
                # Traverse the right tree
                check(node.right)
            elif node.val > p.val and node.val > q.val:
                # Traverse left tree
                check(node.left)
            else:
                self.ancestor = node
                return

        check(root)

        return self.ancestor


# can be dnoe in the normal function no need for helper within, its fine
