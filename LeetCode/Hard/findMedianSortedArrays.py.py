class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums=nums1+nums2
        nums=sorted(nums)
        n = len(nums)
        #print(nums,n)
        if n % 2 == 0:
            i = n//2
            median = (nums[i] + nums[i-1])/2
        else:
            i = (n+1) // 2
            median = nums[i-1]
        return median
