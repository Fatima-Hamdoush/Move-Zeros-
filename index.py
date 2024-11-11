

def moveZeroes(nums):
    zeroes = 0
    for i in range(len(nums)):
        if nums[i] > 0:
            nums[zeroes], nums[i] = nums[i], nums[zeroes]
            zeroes = zeroes + 1
    return nums

#nums = [0, 1, 0, 3, 12]
#print(moveZeroes(nums))
print(moveZeroes([34,2,0,5,0,7,0,0]))


            