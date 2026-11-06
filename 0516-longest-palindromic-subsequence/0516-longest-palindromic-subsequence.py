class Solution(object):
    def longestPalindromeSubseq(self, s):
        rev_s = s[::-1]
        m = len(s)
        n = len(rev_s)
        dp = [[0]*(n+1) for _ in range(m+1)]
        for i in range(m-1,-1,-1):
            for j in range(n-1,-1,-1):
                if s[i] == rev_s[j]:
                    dp[i][j] = 1+ dp[i+1][j+1]
                else:
                    dp[i][j] = max(dp[i+1][j],dp[i][j+1])
        return dp[0][0]
        