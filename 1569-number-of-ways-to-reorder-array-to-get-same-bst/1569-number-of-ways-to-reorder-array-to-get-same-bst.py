class Solution:
    def numOfWays(self, nums: List[int]) -> int:
        mod, n = 10**9 + 7, len(nums)
        born = [-1] * (n + 2)  # insertion time of each value; the walls 0 and n + 1 come before everything
        for t, x in enumerate(nums):
            born[x] = t

        sizes, stack = 1, [0]  # product of subtree sizes mod p; values with increasing insertion times
        for v in range(1, n + 2):
            while born[stack[-1]] > born[v]:  # v is the right wall of the value on top
                stack.pop()
                sizes = sizes * (v - stack[-1] - 1) % mod  # and the value below it is the left wall
            stack.append(v)

        fact = 1
        for k in range(2, n + 1):
            fact = fact * k % mod
        return (fact * pow(sizes, -1, mod) - 1) % mod