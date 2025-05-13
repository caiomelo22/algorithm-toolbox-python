# Time Complexity O(n)
# Space Complexity O(h) where h is the height

def inorderTraversal(root):
    result = []

    def dfs(node):
        if not node:
            return
        dfs(node.left)
        result.append(node.val)
        dfs(node.right)

    dfs(root)
    return result