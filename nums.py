class Solution:
    def small(nums,r):
        p=0
        for i in nums:
            if (i<r and i!=r):
                p=p+i
        return p
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        kums=[]
        l=0
        for i in nums:
            l=small(nums,i) 
            kums.append(l)
        return kums
            
            
        
