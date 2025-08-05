def isSorted(numbers):
    index = 0 #starting index at 0 to review first position in list
    while index < len(numbers) - 1:
        if numbers[index] > numbers[index + 1]:
            return False
        index += 1 # look at next position in the list
    return True

"""random lists with numbers"""
list1 = []
list2 = [7, 9]
list3 = [1, 2, 3, 4]
list4 = [0, 2, 3, 15]
list5 = [5, 5, 3, 1]
list6 = [1, 4, 2, 5]
list7 = [2, 9, 4, 3]
list8 = [8, 8, 8, 7]

print("List 1 is sorted:", isSorted(list1))
print("List 2 is sorted:", isSorted(list2))
print("List 3 is sorted:", isSorted(list3))
print("List 4 is sorted:", isSorted(list4))
print("List 5 is sorted:", isSorted(list5))
print("List 6 is sorted:", isSorted(list6))
print("List 7 is sorted:", isSorted(list7))
print("List 8 is sorted:", isSorted(list8))

