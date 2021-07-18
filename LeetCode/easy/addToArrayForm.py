class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        i = "".join([str(j) for j in num])
        total = str(int(i) + k)
        res=[int(j) for j in total]
        return res
