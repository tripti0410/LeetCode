"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root:
            return []
        current_level, next_level, result= ([root], [], [[root.val]])
        while current_level:
            temp = current_level.pop(0)
            if temp.children:
                next_level += temp.children

            if not current_level and next_level:
                current_level, next_level = next_level, current_level
                result.append([each.val for each in current_level])
        return result
