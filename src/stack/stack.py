# Time Complexity O(n)
# Space Complexity O(n)

def isValid(s: str) -> bool:
    stack = []
    hashmap = {'(': ')', '{': '}', '[': ']'}

    for c in s:
        if c in hashmap:
            stack.append(hashmap[c])
        elif not stack or stack.pop() != c:
            return False

    return len(stack) == 0