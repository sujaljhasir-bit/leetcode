"""
LeetCode 1 - Two Sum
Link: https://leetcode.com/problems/two-sum/
Difficulty: Easy
Tags: array, hash-map
Status: needs-revision

Approach: Store each number's index in a dict; for each x, check if target - x was already seen.
Time: O(n)   Space: O(n)
Mistake/Note: Check the complement BEFORE inserting the current number.
"""

def twoSum(nums, target):
    seen = {}
    for i, x in enumerate(nums):
        if target - x in seen:
            return [seen[target - x], i]
        seen[x] = i
