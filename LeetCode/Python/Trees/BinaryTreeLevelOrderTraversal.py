# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from typing import Optional, List

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        queue = [root]
        level_map = {root: 0}
        result = []

        while queue:
            node = queue.pop(0)
            lvl = level_map[node]

            # Extend result list to fit current level
            if len(result) <= lvl:
                result.append([])

            result[lvl].append(node.val)

            if node.left:
                queue.append(node.left)
                level_map[node.left] = lvl + 1
            if node.right:
                queue.append(node.right)
                level_map[node.right] = lvl + 1

        return result

#Done breadth first
#attempt a depth first search