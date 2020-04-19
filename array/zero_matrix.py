from typing import List


class Solution:class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        pass


if __name__ == "__main__":
    import cProfile

    pr = cProfile.Profile()
    pr.enable()
    x = Solution()
    p = x.lengthOfLongestSubstring("abcabcbb")
    print("ans ", p)
    assert p == 3
    p = x.lengthOfLongestSubstring("bbbbb")
    print("ans ", p)
    assert p == 1
    p = x.lengthOfLongestSubstring("pwwkew")
    print("ans ", p)
    assert p == 3
    pr.disable()
    pr.print_stats(sort="calls")
