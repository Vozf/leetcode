from collections import defaultdict
class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        if len(s) < k:
            return False
        letter_count = defaultdict(lambda: 0)
        for char in s:
            letter_count[char] += 1
        num_odd = sum(count%2 == 1 for count in letter_count.values())
        if num_odd > k:
            return False
        else:
            return True


        
