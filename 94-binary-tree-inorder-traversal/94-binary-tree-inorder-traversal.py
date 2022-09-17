# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        root_stack, visited = [], []
        c = 0
        while True:
            if root and root not in visited:
                root_stack.append(root)
                root = root.left                
            elif root and root in visited:
                root = root.right
            else:
                try:
                    root = root_stack.pop()
                    visited.append(root)
                except IndexError:
                    break
        return [node.val for node in visited]