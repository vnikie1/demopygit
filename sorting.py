def bubble_sort(nums):
    for i in range(len(nums) - 1, 0, -1):
        for j in range(i):
            if nums[j] > nums[j + 1]:
                temp = nums[j]
                nums[j] = nums[j + 1]
                nums[j + 1] = temp


def selection_sort(nums):
    for i in range(len(nums)-1):
        pos = i
        for j in range(i,len(nums),1):
            if nums[j] < nums[pos]:
                pos = j

        temp = nums[i]
        nums[i] = nums[pos]
        nums[pos] = temp
        print(nums)



numbers = [24, 34, 1, 11, 88]
selection_sort(numbers)
print(numbers)
