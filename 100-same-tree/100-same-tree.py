# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def bfs_check(p,q):
            is_same = True
            if p and q:
                if p.val == q.val:
                    is_same = bfs_check(p.left, q.left) & bfs_check(p.right, q.right)
                else:
                    return False
            elif (not p and q) or (not q and p):
                return False
            return is_same
        return bfs_check(p,q)
                
                    