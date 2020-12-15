""" Test.assert_equals(sorted(two_sum([1,2,3], 4)), [0,2])
Test.assert_equals(sorted(two_sum([1234,5678,9012], 14690)), [1,2])
Test.assert_equals(sorted(two_sum([2,2,3], 4)), [0,1]) """

def two_sum(numbers, target):
    for i in range(len(numbers)):
        for j in range(1, len(numbers)):
            if numbers[i] + numbers[j] == target:
               return (i, j)


print(two_sum([1,2,3],0))
print(two_sum([1234,5678,9012], 14690))
print(two_sum([2,2,3], 4))

