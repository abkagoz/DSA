class Solution:
    ## not
    def findMin(self, nums: List[int]) -> int:
            minimum = nums[0]
            l, r = 0, len(nums) - 1

            while l <= r:
                mid = (l + r) // 2
                minimum = min(minimum, nums[mid])
                if nums[mid] > nums[r]:
                    l = mid + 1
                elif nums[mid] <= nums[r]:
                    r = mid - 1
                elif nums[mid] <= nums[l]:
                    r = mid
                else: break
            return minimum