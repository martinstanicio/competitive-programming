class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1

        a, b = 1, 2

        for _ in range(2, n):
            a, b = b, a + b

        return b


if __name__ == "__main__":
    n = int(input())

    answer = Solution().climbStairs(n)

    print(answer)
