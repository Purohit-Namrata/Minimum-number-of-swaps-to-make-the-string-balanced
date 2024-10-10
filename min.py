class Solution:
    def minSwaps(self, s:str)->int:
        imbalance=0
        for i in s:
            if i=='[':
                imbalance+=1
            elif imbalance:
                imbalance-=1
        
        return (imbalance+1)//2
    
s=Solution()
print(s.minSwaps("][]["))