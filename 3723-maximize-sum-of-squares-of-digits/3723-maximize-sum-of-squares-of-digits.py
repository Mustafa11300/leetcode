class Solution(object):
    def maxSumOfSquares(self, num, sum):
        if sum > 9 * num:
            return ""
        k, r = divmod(sum, 9)
        res = "9" * k + (str(r) if r else "")
        return res + "0" * (num - len(res))