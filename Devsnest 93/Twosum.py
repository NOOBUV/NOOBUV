class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic={}
        for index,i in enumerate(nums):
            a=target-i
            if a in dic:
                return [dic[a],index]
            else:
                dic[i]=index
        return []