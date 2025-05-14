# Time Complexity O(n)
# Space Complexity O(n)

from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        memo = dict()

        def robRecursive(curr_idx: int) -> int:
            if curr_idx >= len(nums):
                return 0
            
            if curr_idx not in memo:
                memo[curr_idx] = max(robRecursive(curr_idx + 1), robRecursive(curr_idx + 2) + nums[curr_idx])

            return memo[curr_idx]

        most_revenue = robRecursive(0)

        return most_revenue