class Solution:
    # @param A : integer
    # @param B : integer
    # @return an integer
    res_count = 0

    def convert(self, list):

        # Converting integer list to string list
        # and joining the list using join()
        res = int("".join(map(str, list)))

        return res

    def find_nums(self, n, target_sum, nums, k, dp):

        if not (target_sum >= 0 and n >= 0):
            return 0

        if dp[target_sum][n] == -1:

            iter_nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]

            if len(nums) != 0:
                iter_nums.append(0)

            if len(nums) != 0:
                res = self.convert(nums)

                # if int(res / 1000000007) > 0:
                #     return 0

            if target_sum == 0 and len(nums) == k:
                return 1

            if target_sum < 0:
                return 0

            if n == 0:
                return 0

            l = 0
            for i in iter_nums:
                nums.append(i)
                l += self.find_nums(n - 1, target_sum - i, nums, k, dp)
                nums.pop(-1)
            dp[target_sum][n] = l

        return dp[target_sum][n]

    def solve(self, A, B):
        dp = [[-1 for x in range(A + 1)] for y in range(B + 1)]
        self.find_nums(A, B, [], A, dp)
        return dp[B][A] % 1000000007


if __name__ == "__main__":
    x = Solution()
    p = x.solve(75, 22)
    print("ans ", p)
    assert p == 4
