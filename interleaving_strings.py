class Solution:
    # https://www.interviewbit.com/problems/interleaving-strings/
    # @param A : string
    # @param B : string
    # @param C : string
    # @return an integer
    def find_iterleaving(self, a, a_index, b, b_index, c, c_index):

        # all are processed
        if a_index == len(a) and b_index == len(b) and c_index == len(c):
            return 1

        # b is left un processed
        if a_index == len(a) and c_index == len(c):
            return 0

        # a is left un processed
        if b_index == len(b) and c_index == len(c):
            return 0

        if a[a_index] == c[c_index]:
            x = self.find_iterleaving(a_index + 1, a, b_index, b, c, c_index + 1)

        if b[b_index] == c[c_index]:
            y = self.find_iterleaving(a_index, a, b_index + 1, b, c, c_index + 1)

        return x or y
        
    def isInterleave(self, A, B, C):
        return self.find_iterleaving(A, 0, B, 0, C, 0)


if __name__ == "__main__":
    import cProfile

    pr = cProfile.Profile()
    pr.enable()
    x = Solution()
    p = x.isInterleave("aabcc", "dbbca", "aadbbcbcac")
    print("ans ", p)
    assert p == 1
    x = Solution()
    p = x.isInterleave("aabcc", "dbbca", "aadbbbaccc")
    print("ans ", p)
    assert p == 0
    x = Solution()
    p = x.isInterleave("aabb", "aabb", "aaaabbbb")
    print("ans ", p)
    assert p == 1
    x = Solution()
    p = x.isInterleave("aabcc", "bbca", "aabbcbcac")
    print("ans ", p)
    assert p == 1
    pr.disable()
    # after your program ends
    pr.print_stats(sort="calls")
