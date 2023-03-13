class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        nums = list(set(nums))
        if len(nums)>=3:
            maxNum = max(nums)
            nums.remove(maxNum)
            secondMax =  max(nums)
            nums.remove(secondMax)
            return max(nums)
        else:
            return (max(nums))