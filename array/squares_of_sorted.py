class Solution:
    def sortedSquares(self, nums: [int]) -> [int]:
        map_n = map(lambda x: x*x, nums)
        return sorted(map_n)


nums1 = [-3, 2, 1]  # 1, 4, 9
nums2 = [-3]  # 9
nums3 = [3, 2, 1]  # 1, 4, 9
nums4 = [1, 5, -1]

sol = Solution()
print(sol.sortedSquares(nums1))
print(sol.sortedSquares(nums2))
print(sol.sortedSquares(nums3))
print(sol.sortedSquares(nums4))

