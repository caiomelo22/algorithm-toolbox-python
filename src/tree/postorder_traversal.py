# Time Complexity O(n)
# Space Complexity O(h) where h is the height

def postorderTraversal(root):
    result = []

    def dfs(node):
        if not node:
            return
        dfs(node.left)
        dfs(node.right)
        result.append(node.val)

    dfs(root)
    return result
