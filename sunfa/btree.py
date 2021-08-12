# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def preorderTraversal(self, root: TreeNode):
        res = list()

        def preorder(root: TreeNode):
            if not root:
                return
            res.append(root.val)
            preorder(root.left)
            preorder(root.right)

        preorder(root)

        return res

    def inorderTraversal(self, root: TreeNode):

        res = list()

        def inorder(root):
            if not root:
                return

            inorder(root.left)
            res.append(root.val)
            inorder(root.right)

        inorder(root)

        return res

    def postorderTraversal(self, root: TreeNode):
        res = list()

        def postorder(root):
            if not root:
                return
            postorder(root.left)
            postorder(root.right)
            res.append(root.val)

        postorder(root)
        return res


