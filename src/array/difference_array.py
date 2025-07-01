def arrayManipulation(n, queries):
    array = [0] * (n + 1)

    for a, b, k in queries:
        array[a-1] += k
        array[b] -= k

    max_val = 0
    current = 0

    for i in range(0, n):
        current += array[i]
        max_val = max(max_val, current)

    return max_val