# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # @param A : root node of tree
    # @param B : integer
    # @param C : integer
    # @return an integer
    def find_ancestor_path(self, root, node, path):

        path.append(root.val)
        if root.val == node:
            return path[:]

        path1 = path2 = []
        if root.left != None:
            path1 = self.find_ancestor_path(root.left, node, path)
        if root.right != None:
            path2 = self.find_ancestor_path(root.right, node, path)
        path.pop(-1)

        if not path1 and not path2:
            return []

        if not path1:
            return path2
        else:
            return path1

    def lca(self, A, B, C):
        path1 = self.find_ancestor_path(A, B, [])
        path2 = self.find_ancestor_path(A, C, [])

        if not path1 or not path2:
            return -1

        path1.append(B)
        path2.append(C)

        if len(path1) < len(path2):
            smaller = path1
            bigger = path2
        else:
            smaller = path2
            bigger = path1

        for i in range(len(smaller)):
            if smaller[i] != bigger[i]:
                break
            lca = smaller[i]

        return lca


if __name__ == "__main__":
    import cProfile

    pr = cProfile.Profile()
    pr.enable()
    x = Solution()
    root = TreeNode(331)
    root.left = TreeNode(1)
    root.right = TreeNode(4)
    root.left.left = TreeNode(11)
    root.left.right = TreeNode(41)
    root.right.left = TreeNode(14)
    root.right.right = TreeNode(44)
    root.left.right.left = TreeNode(2)
    root.right.right.right = TreeNode(3)
    p = x.lca(root, 2, 3)
    print("ans ", p)
    assert p == 331
    root = TreeNode(1)
    # root.left = TreeNode(1)
    # root.right = TreeNode(1)
    p = x.lca(root, 1, 1)
    print("ans ", p)
    assert p == 1
    pr.disable()
    # after your program ends
    pr.print_stats(sort="calls")

"""
3 1 1 -1
1
1
"""
