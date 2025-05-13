# Time Complexity O(n)
# Space Complexity O(k) where k is the number of unique chars (at most 128 for ASCII, 256 for extended ASCII)

def lengthOfLongestSubstring(s: str) -> int:
    longest = 0
    last_non_duplicate = 0
    hashmap = dict()

    for i in range(len(s)):
        letter = s[i]

        if letter in hashmap:
            last_non_duplicate = max(hashmap[letter] + 1, last_non_duplicate)
            
        longest = max(i - last_non_duplicate + 1, longest)
        hashmap[letter] = i

    return longest