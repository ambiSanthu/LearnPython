class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        l=len(s)-1
        for i in range((l+1)//2):
            temp=s[l]
            s[l]=s[i]
            s[i]=temp
            i += 1;
            l -= 1;
