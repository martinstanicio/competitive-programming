from itertools import pairwise


class Solution:
    def generate(self, numRows: int) -> list[list[int]]:
        pascal = [[1]]

        for _ in range(1, numRows):
            pascal += [[1] + [sum(p) for p in pairwise(pascal[-1])] + [1]]

        return pascal


if __name__ == "__main__":
    numRows = int(input())

    answer = Solution().generate(numRows)

    print(answer)
