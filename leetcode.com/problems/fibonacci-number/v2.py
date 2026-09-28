from functools import lru_cache


class Solution:
    @lru_cache(maxsize=2)  # noqa: B019
    def fib(self, n: int) -> int:
        if n in (0, 1):
            return n

        return self.fib(n - 1) + self.fib(n - 2)


if __name__ == "__main__":
    n = int(input())

    answer = Solution().fib(n)

    print(answer)
