class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        if len(piles)==3:
            return piles[1]
        ans=0
        itr=0
        l=len(piles)-2
        while l>=0 and itr<len(piles)//3:
            ans+=piles[l]
            l-=2
            itr+=1
        return ans