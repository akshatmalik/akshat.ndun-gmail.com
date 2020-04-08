class Solution:
    """
    https://www.interviewbit.com/problems/palindrome-partitioning-ii/
    """
    def is_palindrome(self, test_string, start_index, end_index, dp_is_palindrome) -> bool:
        while start_index < end_index:
            if test_string[start_index] != test_string[end_index]:
                return False
            start_index += 1
            end_index -= 1
        return True

    def recur(self, test_string, start_index, end_index, dp, dp_is_palindrome):
        if start_index >= end_index or self.is_palindrome(test_string, start_index, end_index, dp_is_palindrome):
            return 0

        if dp[start_index][end_index] == -1:
            minimum_cuts = len(test_string) - 1
            for i in range(start_index, end_index+1):
                if self.is_palindrome(test_string, start_index, i, dp_is_palindrome):
                    minimum_cuts = min(minimum_cuts, 1 + self.recur(test_string, i+1, end_index, dp, dp_is_palindrome))
            dp[start_index][end_index] = minimum_cuts

        return dp[start_index][end_index]

    def minCut(self, A):
        n = len(A)
        dp = [[-1 for _ in range(n)] for _ in range(n)]
        dp_is_palindrome = [[-1 for _ in range(n)] for _ in range(n)]
        return self.recur(A, 0, len(A) - 1, dp, dp_is_palindrome)



if __name__ == "__main__":
    import cProfile

    pr = cProfile.Profile()
    pr.enable()
    x = Solution()
    p = x.minCut("aabbcc")
    print("ans ", p)
    assert p == 2
    p = x.minCut("daad")
    print("ans ", p)
    assert p == 0
    p = x.minCut("abcba")
    print("ans ", p)
    assert p == 0
    p = x.minCut("abc")
    print("ans ", p)
    assert p == 2
    pr.disable()
    # after your program ends
    pr.print_stats(sort="calls")
