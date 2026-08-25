class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        x = 0
        for n in nums:
            q, r = divmod(n, k)
            if r == 0:
                i = q - 1
                if i >= 0:
                    x |= 1 << i

        x += 1
        return (x & -x).bit_length() * k