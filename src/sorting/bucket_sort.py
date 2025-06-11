from typing import List

def topKFrequent(nums: List[int], k: int) -> List[int]:
    # Step 1: Count frequencies
    freq = dict()

    for num in nums:
        if num not in freq:
            freq[num] = 0
            
        freq[num] += 1

    # Step 2: Bucket sort by frequency
    bucket = [[] for _ in range(len(nums) + 1)]
    for num, count in freq.items():
        bucket[count].append(num)

    # Step 3: Collect top k frequent elements
    res = []
    for i in range(len(bucket) - 1, 0, -1):
        for num in bucket[i]:
            res.append(num)
            if len(res) == k:
                return res
