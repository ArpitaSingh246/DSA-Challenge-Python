class Solution(object):
    def runningSum(self, nums):
        '''sum = 0
        list_sum = []
        for i in range(len(nums)):
            sum += nums[i]
            list_sum.append(sum)
        return list_sum'''
        
        
        def calculate(i):
 
            if i == len(nums):
                return
            nums[i] = nums[i] + nums[i - 1]
            calculate(i + 1)

        calculate(1)
        return nums
        