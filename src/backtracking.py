# Time Complexity O(N^T) Where N is the number of candidates and T the target
# Space Complexity O(M*L) Where M is the number of combinations and L the average length

from typing import List

class Solution:
    def backtracking(self, start: int, candidates: List[int], target: int, curr_sum: int, curr_numbers: List[int]) -> None:
        if curr_sum == target:
            self.results.append(curr_numbers[:])
            return
        elif curr_sum > target:
            return
        
        for i in range(start, len(candidates)):
            curr_numbers.append(candidates[i])
            self.backtracking(i, candidates, target, curr_sum + candidates[i], curr_numbers)
            curr_numbers.pop()
            
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        self.results = []

        self.backtracking(0, candidates, target, 0, [])

        return self.results
        