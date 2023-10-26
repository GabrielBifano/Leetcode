# Move Zeroes
# Easy

def moveZeroes(self, nums: 'list[int]') -> None:

    zcounter = 0
    insert_here = 0

    for i in range(0, len(nums)):
        if nums[i] == 0:
            zcounter += 1
            continue
        nums[insert_here] = nums[i]
        insert_here += 1

    for i in range(insert_here, len(nums)):
        nums[i] = 0