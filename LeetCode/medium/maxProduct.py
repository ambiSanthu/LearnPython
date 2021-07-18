class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maxprod=nums[0]
        size=len(nums)
        for i in range(size):
            prod = nums[i]
            if prod > maxprod:
                maxprod = prod
            for j in range(i+1,size):
                prod = prod * nums[j]
                if prod > maxprod:
                    maxprod = prod
        return maxprod
