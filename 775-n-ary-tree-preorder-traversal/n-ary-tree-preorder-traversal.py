"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        if root is None:
            return []
            
        result = []
        # we are using queue like list not actual queue
        queue = [root]
        while queue:
            current_node = queue.pop(0)
            result.append(current_node.val)
            queue = current_node.children + queue

        return result