'''
Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.'''
def searchIndex(nums, target):
    mid = (len(nums)-1) // 2
    if nums[mid] == target:
        return mid
    elif nums[mid] > target:
        return searchIndex(nums, target, mid - 1)
    else:
        return searchIndex(nums, target, mid + 1)

searchIndex([2, 3, 4, 5, 6], 6)