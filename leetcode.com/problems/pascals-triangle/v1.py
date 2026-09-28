from itertools import pairwise


class Solution:
    def generate(self, numRows: int) -> list[list[int]]:
        if numRows == 1:
            return [[1]]

        prev = self.generate(numRows - 1)

        return prev + [[1] + [sum(p) for p in pairwise(prev[-1])] + [1]]


if __name__ == "__main__":
    numRows = int(input())

    answer = Solution().generate(numRows)

    print(answer)
