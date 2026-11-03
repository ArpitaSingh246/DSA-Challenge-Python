class Solution(object):
    def minStartValue(self, nums):
        
        summ = 0
        minSum = 0
        for num in nums:
            summ += num
            minSum = min(minSum, summ)
        return 1 - minSum
