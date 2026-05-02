# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        return self._isBalanced(root)[1]
        
    def _isBalanced(self, root: Optional[TreeNode]) -> List[int, bool]:
        if not root:
            return 0, True
        
        left_height, is_left_balanced = self._isBalanced(root.left)
        if not is_left_balanced:
            return -1, False

        right_height, is_right_balanced = self._isBalanced(root.right)

        if not is_right_balanced:
            return -1, False

        if abs(left_height - right_height) > 1:
            return -1, False
            
        return 1 + max(left_height, right_height), True
        
