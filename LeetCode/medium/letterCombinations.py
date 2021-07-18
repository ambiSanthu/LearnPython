class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        tel = {'2':'abc','3':'def','4':'ghi','5':'jkl',\
               '6':'mno','7':'pqrs','8':'tuv','9':'wxyz'}
        res = []
        if digits:
            res = list(tel[digits[0]])
        for i in range(1,len(digits)):
            #print(i,res)
            output = []
            for j in res:
                #print(j)
                for k in tel[digits[i]]:
                    tmp = j + k
                    #print(tmp)
                    output.append(tmp)
                res = output
        return res
