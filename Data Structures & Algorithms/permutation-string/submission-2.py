from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        print(len(s1))
        window_size = len(s1)
        s1_hashmap = Counter(s1)

        # Slide to the right
        for i in range(len(s2) - window_size + 1):
            window = s2[i:i + window_size]
            print(window)
            window_hashmap = Counter(window)
            if window_hashmap == s1_hashmap:
                return True
        return False
