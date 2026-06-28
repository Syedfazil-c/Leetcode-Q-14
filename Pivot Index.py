nums =[1,3,7,6,5,6]
def pivotIndex(nums):
    total = sum(nums)
    left =0
    for i in range (len(nums)):
        right = total - left - nums[i]
        if left == right:
            return i
        left +=nums[i]
    return -1
print(pivotIndex(nums))
