from itertools import pairwise


class Solution:
    def generate(self, numRows: int) -> list[list[int]]:
        dp = [[1]] + [[]] * (numRows - 1)

        for i in range(1, numRows):
            dp[i] = [1] + [sum(p) for p in pairwise(dp[i - 1])] + [1]

        return dp


if __name__ == "__main__":
    numRows = int(input())

    answer = Solution().generate(numRows)

    print(answer)
