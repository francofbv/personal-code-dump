'''
Given two 0-indexed integer arrays nums1 and nums2, return a list answer of size 2 where:

answer[0] is a list of all distinct integers in nums1 which are not present in nums2.
answer[1] is a list of all distinct integers in nums2 which are not present in nums1.
Note that the integers in the lists may be returned in any order.
'''
def findDifference (nums1, nums2):
    nums1 = set(nums1)
    nums2 = set(nums2)
    return [list(nums1 - nums2), list(nums2 - nums1)]
print(findDifference([1, 2, 3], [2, 4, 6]))