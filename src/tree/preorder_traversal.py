# Time Complexity O(n)
# Space Complexity O(h) where h is the height

def preorderTraversal(root):
    result = []

    def dfs(node):
        if not node:
            return
        result.append(node.val)
        dfs(node.left)
        dfs(node.right)

    dfs(root)
    return result