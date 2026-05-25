
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    
class Solution:
    def pathSum(self, root, targetSum):
        paths = []
        def ps(node, target, path):
            nonlocal paths
            if not node:
                return 
            
            if not node.left and not node.right:
                if node.val == target:
                    paths.append(path + [node.val])
                return
            
            ps(node.left, target - node.val, path + [node.val])
            ps(node.right, target - node.val, path + [node.val])
        
        ps(root, targetSum, [])

        return paths