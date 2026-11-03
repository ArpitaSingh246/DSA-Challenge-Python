class Solution(object):
    def runningSum(self, nums):
        sum = 0
        list_sum = []
        for i in range(len(nums)):
            sum += nums[i]
            list_sum.append(sum)
        return list_sum

        