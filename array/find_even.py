class Solution:
    def findNumbers(self, nums: [int]) -> int:
        cnt = 0
        for n in nums:
            if len(str(n))%2 == 0:
                cnt += 1
        return cnt


c = Solution()
print(c.findNumbers([12,345,2,6,7896]))