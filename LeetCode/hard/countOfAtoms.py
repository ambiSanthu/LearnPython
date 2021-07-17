class Solution:
    def countOfAtoms(self, formula: str) -> str:
        def getdigits(formula,ind):
            tmp = ""
            itr=ind+1
            while(itr < len(formula)):
                if formula[itr].isdigit():
                        tmp=tmp+formula[itr]
                        itr=itr+1
                else:
                    break   
            if tmp == "":
                num=1
            else:
                num=int(tmp)
            #print(num,(itr-ind))
            return num,(itr-ind)

        if "(" in formula:
            while(True):
                length = len(formula)
                try:
                    ind = formula.index(")")
                except:
                    break

                num,itr = getdigits(formula,ind)
                if num == 1:
                    formula=formula.replace("(","").replace(")","")
                    continue

                subatom = ""
                for j in range(ind,-1,-1):
                    if formula[j] == "(":
                        subatom=formula[j]+subatom
                        break
                    else:
                        subatom=formula[j]+subatom

                #formula=formula.replace(subatom+str(num),"")
                subatom_mod=subatom.replace("(","").replace(")","")
                exp = ""
                #print(subatom_mod)
                i=0
                while(i<len(subatom_mod)):
                    if (i+1) >= len(subatom_mod):
                        if subatom_mod[i].isdigit():
                            n = int(subatom_mod[i])
                           # print(exp,n,num)
                            exp = exp+str(n*num)
                        else:
                            exp = exp+subatom_mod[i]+str(num)
                        break
                    elif subatom_mod[i+1].isdigit():
                        n,itr = getdigits(subatom_mod,i)
                        exp = exp+subatom_mod[i]+str(n*num)
                        i=i+itr
                    elif subatom_mod[i+1].isupper():
                        exp = exp+subatom_mod[i]+str(num)
                        i=i+1
                    elif subatom_mod[i+1].islower():
                        exp = exp+subatom_mod[i]
                        i=i+1
                #print(exp)
                formula=formula.replace(subatom+str(num),exp)
        print(formula)

        #"B78Be1950He663O1521"

        import re
        pattern="[A-Za-z]*[0-9]+"
        m= re.findall(pattern, formula)
        m=sorted(m)

        for f in m:
            formula=formula.replace(f,"")
        #print("leftout: ",formula)  

        if not formula == "":
            m.append(formula)

        #print(formula)
        print(m)
        df=dict()

        def updatedict(key,value,df):
            if key and value:
                if key in df.keys():
                    df[key] = df[key] + value
                else:
                    df[key] = value
                #print(key,value)
        for i in m:
            key=""
            value = ""
            while(len(i)>0):
               # pattern="[A-Z][a-z]*[0-9]+"
               # n = re.findall(pattern, i)
                #print("Start i : ",i)
                if len(i) == 1:
                    key = i
                    value = 1
                    i = ""
                    updatedict(key,value,df)
                    #print(key,value)
                elif len(i) == 2 and i[1].islower():
                        key = i
                        value = 1
                        i = ""
                        updatedict(key,value,df)
                        #print(key,value)
                else:
                    n = re.findall("[A-Z][a-z]*[0-9]+", i)
                    if len(n) > 0:
                        key = re.findall("[A-Z][a-z]*",n[0])[0]
                        value = int(re.findall("[0-9]+",n[0])[0])
                        i = i.replace(n[0],"")
                        updatedict(key,value,df)
                        #print(key,value)
                    else:
                        n = re.findall("[A-Z][a-z]*",i)
                        for key in n:
                            updatedict(key,1,df)
                            i = i.replace(key,"")
                            #print(key,value)
                        n = re.findall("[A-Z]",i)
                        for key in n:
                            updatedict(key,1,df)
                            i = i.replace(key,"")
                            ####print(key,value)


        result=""
        for k in sorted(df.keys()):
            val = ""
            if df[k]!=1:
                val=str(df[k])
            result=result+k+val
            #print(k,df[k])
        #print(result)
        result=result.lstrip(string.digits)
        return result
