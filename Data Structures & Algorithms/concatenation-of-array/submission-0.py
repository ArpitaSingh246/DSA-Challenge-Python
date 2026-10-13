class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        '''return 2*nums'''
        '''return nums + nums'''
        ans = nums.copy()
        for i in range(len(nums)):
            if ans[i] == nums[i]:
                return nums + ans