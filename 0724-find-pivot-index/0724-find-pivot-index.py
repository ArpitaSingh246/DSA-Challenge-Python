class Solution(object):
    def pivotIndex(self, nums):
        '''for i in range(len(nums)):
            left_sum = 0
            for left in range(0,i):
                left_sum += nums[left]
            right_sum = 0
            for right in range(i+1,len(nums)):
                right_sum += nums[right]
            if left_sum == right_sum:
                return i
        return -1 '''

        
        total_sum = sum(nums)
        left_sum = 0
        for i in range(len(nums)): 
            if left_sum == (total_sum - left_sum - nums[i]):
                return i   
            left_sum += nums[i] 
            
        return -1
