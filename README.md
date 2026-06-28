Find Pivot Index

Problem

Given an integer array nums, return the leftmost pivot index.

A pivot index is an index where the sum of all elements to the left is equal to the sum of all elements to the right.

If no such index exists, return -1.

Approach

- Calculate the total sum of the array.
- Initialize left sum as 0.
- Traverse the array from left to right.
- For each index, calculate the right sum using:
  right = total - left - nums[i]
- Compare the left sum and right sum.
- If they are equal, return the current index.
- Otherwise, add the current element to the left sum and continue.
- If no pivot index is found, return -1.

Complexity

Time Complexity: O(n)

Space Complexity: O(1)

Key Insight

Instead of calculating the left and right sums separately for every index, keep a running left sum and compute the right sum using the total sum.

This avoids repeated calculations and makes the solution efficient.

Example

Input:

nums = [1,7,3,6,5,6]

Output:

3

Explanation:

Total Sum = 28

At index 3:

Left Sum = 1 + 7 + 3 = 11

Right Sum = 5 + 6 = 11

Since both sums are equal, the pivot index is 3.

Input:

nums = [1,2,3]

Output:

-1

Explanation:

No index has equal left and right sums.

Code

def pivotIndex(nums):

    total = sum(nums)
    
    left = 0

    for i in range(len(nums)):
    
        right = total - left - nums[i]

        if left == right:
        
            return i

        left += nums[i]

    return -1

