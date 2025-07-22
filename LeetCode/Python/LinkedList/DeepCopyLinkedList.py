"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""


class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':

        ogHead = head
        originalCopy = head

        randomDict = {}

        while originalCopy:
            new_node = Node(originalCopy.val)
            randomDict[originalCopy] = new_node
            originalCopy = originalCopy.next

        while head:
            new_node = randomDict[head]
            new_node.random = randomDict.get(head.random)
            new_node.next = randomDict.get(head.next)
            head = head.next

        return randomDict.get(ogHead)