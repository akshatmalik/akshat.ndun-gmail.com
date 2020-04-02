class Solution:
    # https://www.interviewbit.com/problems/distinct-subsequences/
    # @param A : string
    # @param B : list of strings
    # @return an integer
    def find_make(self, A, a_index, B, b_index, dp):

        if dp[a_index][b_index] == -1:

            if len(A) == a_index and len(B) == b_index:
                return 1

            if a_index == len(A) and len(B) != b_index:
                return 0

            if a_index != len(A) and len(B) == b_index:
                return 0

            if A[a_index] == B[b_index]:
                dp[a_index][b_index] = self.find_make(A, a_index + 1, B, b_index + 1, dp) + self.find_make(A, a_index + 1, B, b_index, dp)
            else:
                dp[a_index][b_index] = self.find_make(A, a_index + 1, B, b_index, dp)

        return dp[a_index][b_index]

    def numDistinct(self, A, B):
        dp = [[-1 for _ in range(len(B) + 1)] for _ in range(len(A) + 1) ]
        return self.find_make(A, 0, B, 0, dp)


if __name__ == "__main__":
    import cProfile

    pr = cProfile.Profile()
    pr.enable()
    x = Solution()
    p = x.numDistinct("rabbbit", "rabbit")
    print("ans ", p)
    assert p == 3
    x = Solution()
    p = x.numDistinct("abc", "abc")
    print("ans ", p)
    assert p == 1
    x = Solution()
    p = x.numDistinct("cba", "abc")
    print("ans ", p)
    assert p == 0
    pr.disable()
    # after your program ends
    pr.print_stats(sort="calls")
