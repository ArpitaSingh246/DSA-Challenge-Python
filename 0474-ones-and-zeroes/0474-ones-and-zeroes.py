class Solution(object):
    def findMaxForm(self, strs, m, n):
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        for s in strs:
            zeros = s.count('0')
            ones = s.count('1')
            for z in range(m, zeros - 1, -1):
                for o in range(n, ones - 1, -1):
                    dp[z][o] = max(dp[z][o], 1 + dp[z - zeros][o - ones])
                    
        return dp[m][n]
