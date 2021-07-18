class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        index = 1
        if len(nums) == 1:
            return 1
        for i in range(1,len(nums)):
            if nums[i] > nums[i-1]:
                nums[index] = nums[i]
                index += 1
        return index
