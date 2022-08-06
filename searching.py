#linear search

pos = -1

def linear_serach(search, nums):
    for i in range(len(nums)):
        print("inside for i >>" + str(i) + "number checking is >> " + str(nums[i]))
        if nums[i] == search:
            print("inside for i >>" + str(i))
            globals() ['pos'] = i+1
            return True

        elif i == len(nums)-1:
            return False



def binary_search(search, nums):
    l = 0
    u = len(nums) - 1
    for i in range(len(nums)):
        l = i
        m = (l+u)//2
        if nums[m] == search:
            globals() ['pos'] = m+1
            return True
        elif nums[m] < search:
            i = m+1
        else:
            u = m-1




numbers = [34]
search_num = 34
numbers.sort()
print(numbers)
if binary_search(search_num,numbers):
    print("Value found at pos " + str(pos))
else:
     print("Value not found ")








