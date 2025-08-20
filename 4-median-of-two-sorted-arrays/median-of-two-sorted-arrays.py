class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        merged = []

        while nums1 or nums2:
            if nums1 and nums2:
                if nums1[0] > nums2[0]:
                    merged.append(nums2[0])
                    nums2.pop(0)
                else:
                    merged.append(nums1[0])
                    nums1.pop(0)
            elif nums1:
                merged.append(nums1[0])
                nums1.pop(0)
            else:
                merged.append(nums2[0])
                nums2.pop(0)

        n = len(merged)
        
        if len(merged) % 2 == 0:
            return (merged[n // 2] + merged[n // 2 - 1]) / 2
        else:
            return merged[n // 2]