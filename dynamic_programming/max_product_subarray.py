import sys


class Solution:
    """
    https://www.interviewbit.com/problems/max-product-subarray/
    """

    def maxProduct(self, A):
        return self.solve_util(A, 0, -1, 1, 1, 1)

    def solve_util(self, A, current_index, previous_index, max_product, min_product):

        if current_index == len(A):
            return max_product

        if A[current_index] > 0:
            max_product = max(max_product, max_product* A[current_index])
            min_product = min(1, min_product * A[current_index])
        elif A[current_index] < 0:
            pass

        include = exclude = - sys.maxsize
        if previous_index == -1 or product * A[current_index] > product * A[previous_index] :
            include = self.solve_util(A, current_index + 1, current_index, product * A[current_index])
        exclude = self.solve_util(A, current_index + 1, previous_index, product)

        return max(include, exclude)


if __name__ == "__main__":
    import cProfile

    pr = cProfile.Profile()
    pr.enable()
    x = Solution()
    p = x.maxProduct([2, 3, -2, 4], )
    print("ans ", p)
    assert p == 6
    pr.disable()
    # after your program ends
    pr.print_stats(sort="calls")
