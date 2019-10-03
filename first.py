x = 1
y = 2
z = 5

if z <= 1 :
    print("Hey")
else:
    print("Ho")
    
def bubble_sort(nums):  
    swapped = True
    while swapped:
        swapped = False
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                nums[i], nums[i + 1] = nums[i + 1], nums[i]
                swapped = True

def insertion_sort(nums):  
    for i in range(1, len(nums)):
        item_to_insert = nums[i]
        j = i - 1
        while j >= 0 and nums[j] > item_to_insert:
            nums[j + 1] = nums[j]
            j -= 1
        nums[j + 1] = item_to_insert

def selection_sort(nums):  
    for i in range(len(nums)):
        lowest_value_index = i
        for j in range(i + 1, len(nums)):
            if nums[j] < nums[lowest_value_index]:
                lowest_value_index = j
        nums[i], nums[lowest_value_index] = nums[lowest_value_index], nums[i]


array1 = [720, 745, 379, 557, 61, 512, 739, 867, 597, 630, 312, 268, 768, 880, 443]
bubble_sort(array1)
print("Bubble Sort: " + str(array1) + "\n")

array2 = [888, 235, 598, 741, 956, 255, 72, 406, 261, 451, 20, 703, 910, 867, 964]
insertion_sort(array2)
print("Insertion Sort: " + str(array2) + "\n")

array3 = [703, 153, 694, 977, 575, 864, 780, 991, 187, 641, 346, 521, 713, 457, 767]
selection_sort(array3)
print("Selection Sort: " + str(array3) + "\n") 
