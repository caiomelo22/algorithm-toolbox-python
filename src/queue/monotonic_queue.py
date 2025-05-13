# Time Complexity O(n)
# Space Complexity O(k)

from collections import deque
from typing import List

def maxSlidingWindow(nums: List[int], k: int) -> List[int]:
    answer = []
    window = deque()

    for i, num in enumerate(nums):
        while window and window[0] < i - k + 1:
            window.popleft()

        while window and nums[window[-1]] < num:
            window.pop()

        window.append(i)

        if i >= k - 1:
            answer.append(nums[window[0]])

    return answer