"""
You are given the root of a binary search tree (BST) and an integer val.
Find the node in the BST that the node's value equals val and return the subtree rooted with that node. If such a node does not exist, return null.

Example 1:
    Input: root = [4,2,7,1,3], val = 2
    Output: [2,1,3]

Example 2:
    Input: root = [4,2,7,1,3], val = 5
    Output: []
 

Constraints:
    The number of nodes in the tree is in the range [1, 5000].
    1 <= Node.val <= 107
    root is a binary search tree.
    1 <= val <= 107
"""

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def searchBST(self, root, val):
        """
        :type root: Optional[TreeNode]
        :type val: int
        :rtype: Optional[TreeNode]
        """
        while root is not None and root.val != val:
            if root.val > val:
                root = root.left
            else:
                root = root.right
        return root

if __name__ == "__main__":
    root = TreeNode(4)
    root.left = TreeNode(2)
    root.right = TreeNode(7)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(3)

    val = 2
    solution = Solution()
    result = solution.searchBST(root, val)

    if result:
        print(f"Found node with value: {result.val}")
    else:
        print("Node not found")