class Solution:
    def removeDuplicates(self, S: str) -> str:
        stack=[]
        for i in range(len(S)):
            if not stack:
                stack.append(S[i])
            elif stack[-1] == S[i]:
                stack.pop(-1)
            else:
                stack.append(S[i])
            #print(stack)
        #print(str(stack))
        return "".join(stack)
