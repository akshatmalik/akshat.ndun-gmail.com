class Solution:
    # @param A : list of list of integers
    # @return an integer
    # https://www.interviewbit.com/problems/sub-matrices-with-sum-zero/
    x_limit = y_limit = 0

    def is_valid(self, x_index, y_index):
        # boundary conditions
        if x_index >= self.x_limit or y_index >= self.y_limit or x_index <= -1 or y_index <= -1:
            return False
        return True

    def solve_util(self, matrix, x_index, y_index, sum, dp, visited):

        # win
        if sum == 0 and not (x_index == 0 and y_index == 0):
            print("True")
            return 1

        key = "{}|{}|{}".format(x_index, y_index, sum)
        key_index = "{}|{}".format(x_index, y_index)

        if dp.get(key, -1) == -1:
            offsets = [(0, 1), (-1, 0), (1, 0), (0, -1), ]
            include_solutions = exclude_solutions = 0
            for offset in offsets:
                if (not self.is_valid(x_index + offset[0], y_index + offset[1])) or visited.get(key_index, -1) == 0:
                    continue
                print(key_index, visited)
                visited[key_index] = 0
                include_solutions += self.solve_util(matrix, x_index + offset[0], y_index + offset[1],
                                                     sum + matrix[x_index][y_index], dp, visited)
                visited[key_index] = 0
                exclude_solutions += self.solve_util(matrix, x_index + offset[0], y_index + offset[1],
                                                     sum, dp, visited)
                visited[key_index] = -1

            dp[key] = max(include_solutions, exclude_solutions, dp.get(key, -1))

        return dp.get(key, -1)

    def solve(self, A):
        self.x_limit = len(A[0])
        self.y_limit = len(A)
        dp = {}
        visited = {}
        return self.solve_util(A, 0, 0, -1, dp, visited)


if __name__ == "__main__":
    import cProfile

    pr = cProfile.Profile()
    pr.enable()
    x = Solution()
    p = x.solve([
        [-8, 5, 3],
        [3, 7, -8],
        [5, -8, 9]
    ])
    print("ans ", p)
    assert p == 2
    pr.disable()
    # after your program ends
    pr.print_stats(sort="calls")
