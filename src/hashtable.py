# Time Complexity O(n * k log k) with n being the number of strings and k the maximum length of a string
# Space Complexity O(nk)

from typing import List

def groupAnagrams(strs: List[str]) -> List[List[str]]:
    hashmap = dict()

    for s in strs:
        s_sorted = ''.join(sorted(s))

        if s_sorted not in hashmap:
            hashmap[s_sorted] = []

        hashmap[s_sorted].append(s)

    return list(hashmap.values())