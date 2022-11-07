"""
TC - O(n)
SC - O(n)
"""
from collections import Counter


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if nums1 is None or len(nums1) == 0 or nums2 is None or len(nums2) == 0: return []

        # rtnData that we want to return
        rtnData = []

        # To keep the count of each element in nums2
        count = Counter(nums2)

        # Now for each element in first array
        for num in nums1:
            # If count of that element is > 0 we can include it
            if num in count and count[num] > 0:
                rtnData.append(num)
                # Reduce its count by 1 as we included this element once in the rtnData
                count[num] -= 1

        return rtnData