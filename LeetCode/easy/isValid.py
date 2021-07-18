class Solution:
    def isValid(self, s: str) -> bool:

        listp=[s[0]]
        for i in range(1,len(s)):
            if not listp:
                listp.append(s[i])
                continue
            elif s[i] == ')':
                if listp[-1] == '(':
                    listp.pop()
                    continue
            elif s[i] == '}':
                if listp[-1] == '{':
                    listp.pop()
                    continue
            elif s[i] == ']':
                if listp[-1] == '[':
                    listp.pop()
                    continue
            listp.append(s[i])
            #print(listp)   

        if len(listp) == 0:
            return True
        else:
            return False
            
                
