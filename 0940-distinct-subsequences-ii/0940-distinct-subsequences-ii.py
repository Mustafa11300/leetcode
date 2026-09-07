class Solution:
    def distinctSubseqII(self, s):
        MOD = 10**9 + 7
        dp = [0] * (len(s) + 1)
        last = {}
        dp[0] = 1
        
        for i in range(1, len(s) + 1):
            dp[i] = 2 * dp[i - 1] % MOD
            if s[i - 1] in last:
                dp[i] -= dp[last[s[i - 1]] - 1]
            dp[i] = (dp[i] + MOD) % MOD
            last[s[i - 1]] = i
        
        return dp[len(s)] - 1 if dp[len(s)] - 1 >= 0 else MOD - 1