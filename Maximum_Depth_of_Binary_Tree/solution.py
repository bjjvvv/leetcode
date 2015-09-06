'''
Given a binary tree, find its maximum depth.

The maximum depth is the number of nodes along the longest path
from the root node down to the farthest leaf node.
'''

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def maxdep(root):
            if root == None:
                return 0
            l_left = maxdep(root.left)
            l_right = maxdep(root.right)
            return max(l_left, l_right) + 1
        return maxdep(root)

def test():
    print('start test')
    t0 = TreeNode(1)
    t1 = TreeNode(1)
    t2 = TreeNode(1)
    t3 = TreeNode(1)
    t4 = TreeNode(1)
    t5 = TreeNode(1)
    t0.left = t1
    t1.left = t2
    t2.left = t3
    t3.left = t4
    t4.left = t5
    s = Solution()
    print(s.maxDepth(t0) )

test()
