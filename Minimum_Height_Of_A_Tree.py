# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        queue = deque([(root,1)])
        
        while queue:
            for i in range(len(queue)):
                node, depth = queue.popleft()
                if node.left is None and node.right is None:
                    return depth
                if node.left is not None:
                    queue.append((node.left,depth+1))
                if node.right is not None:
                    queue.append((node.right,depth+1))