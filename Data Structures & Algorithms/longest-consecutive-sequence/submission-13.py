class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hash_map=set(nums)
        ans=0

        for num in nums:
            if (num-1) not in hash_map:
                l=0
                while (num+l) in hash_map:
                    l+=1
                ans=max(ans,l)
        return ans