
if __name__ == "__main__":
    import cProfile

    pr = cProfile.Profile()
    pr.enable()
    x = Solution()
    p = x.isInterleave("aabcc", "bbca", "aabbcbcac")
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
    pr.dump_stats("stats")
    pr.print_stats(sort="calls")
