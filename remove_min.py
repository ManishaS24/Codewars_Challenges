
"""Given an array of integers, remove the smallest value. Do not mutate the original array/list. 
If there are multiple elements with the same value, remove the one with a lower index. If you get an empty array/list,
return an empty array/list.Don't change the order of the elements that are left.

Examples
 remove_smallest([1,2,3,4,5]) = [2,3,4,5]
remove_smallest([5,3,2,1,4]) = [5,3,2,4]
remove_smallest([2,2,1,2,1]) = [2,2,2,1] """

""" def remove_smallest(numbers):
    if numbers:
        numbers.remove(min(numbers))
    return numbers
 """

""" def remove_smallest(numbers):
    print(numbers)
    if len(numbers) == 0:
        return numbers
    else:
        numbers.remove(min(numbers))
        print(numbers)
        return numbers """

def remove_smallest(numbers):
    if len(numbers) == 0: 
        return numbers
    i = numbers.index(min(numbers))
    return numbers[0:i] + numbers[i+1:]
    


        

remove_smallest([0, 263, 399, 136, 339, 43, 174])