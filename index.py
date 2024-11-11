

def moveZeroes(nums):
    zeroes = 0
    for i in range(len(nums)):
        if nums[i] > 0:
            nums[zeroes], nums[i] = nums[i], nums[zeroes]
            zeroes = zeroes + 1
    len_no0 = len(nums)-zeroes-1
    for i in range(len_no0):
        if(nums[i]>nums[i+1]):
            nums[i], nums[i+1] = nums[i+1], nums[i]
            

    return nums

nums = [0, 1, 0, 3, 12]
print(moveZeroes(nums))
#print(moveZeroes([34,2,0,5,0,7,0,0]))


            