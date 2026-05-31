# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None

        # RECURSIVE
        # root.left, root.right = root.right, root.left
        # self.invertTree(root.left)
        # self.invertTree(root.right)

        # BFS
        # queue = deque([root])

        # while queue:
        #     node = queue.popleft()
        #     node.left, node.right = node.right, node.left
        #     if node.left:
        #         queue.append(node.left)
        #     if node.right:
        #         queue.append(node.right)

        # ITERATIVE DFS
        array = [root]
        print(root.val)
        while array:
            node = array.pop()
            print(node.val)
            node.left, node.right = node.right, node.left
            if node.left:
                array.append(node.left)
            if node.right:
                array.append(node.right)
        return root



        








        


        