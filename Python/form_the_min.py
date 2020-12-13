""" Given a list of digits, return the smallest number that could be formed 
from these digits, using the digits only once (ignore duplicates).

minValue({5, 7, 5, 9, 7})  ==> return (579) """


""" def min_value(digits):
    # your code here
    uniq_digits = sorted(set(digits))
    # print(uniq_digits)
    min_val = ''.join(str(x) for x in uniq_digits)
    # print(min_val)

    return min_val """

def min_value(digits):
    # your code here
    return int(''.join(map(str, sorted(set(digits)))))
    
print(min_value([1, 9, 3, 1, 7, 4, 6, 6, 7]))