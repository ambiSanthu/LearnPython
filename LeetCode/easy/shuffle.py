class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        size=len(nums)
        res=[]
        for i in range(n):
            index=i
            while (index<size):
                res.append(nums[index])
                index=index+n
        return res
