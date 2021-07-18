class Solution:
    def sampleStats(self, count: List[int]) -> List[float]:
        mode = count.index(max(count))
        total_count = 0
        mini = -1
        maxi = 0
        prod = 0
        if count[0] != 0:
            mini = 0
        for i in range(len(count)):
            total_count = total_count + count[i]
            prod = prod + (count[i] * i)
            if count[i] != 0 and mini == -1:
                mini = i
            if count[i] != 0:
                maxi = i
                
        mean = prod/total_count
        
        mid = (total_count + 1)// 2
        print(total_count,mid)
        total = 0
        for i in range(len(count)):
            total = total + count[i]
            if total == mid:
                if total_count % 2 == 0:
                    n = i+1
                    while (count[n] == 0):
                        n = n+1
                    print(total,mid,i,n)
                    median = (n + i) / 2
                else:
                    median = i
                break
            elif total > mid:
                median = i
                break

            
        return[mini,maxi,mean,median,mode]
                
