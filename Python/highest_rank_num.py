""" test.describe("Example Tests")
test.it("Example Test Case")
test.assert_equals(highest_rank([12, 10, 8, 12, 7, 6, 4, 10, 12]), 12)
test.assert_equals(highest_rank([12, 10, 8, 12, 7, 6, 4, 10, 10]), 10) """

def highest_rank(arr):
    # your code here
    freq_count = {}
    
    #print(len(freq_count))
    for i in arr:
        if len(freq_count) == 0:
            freq_count[i] = 1
        
        elif i not in freq_count.keys():
            freq_count[i] = 1
        else:
            freq_count[i] += 1
    
    print(max_vals)
    print(freq_count)
    return


print(highest_rank([12, 10, 8, 12, 7, 6, 4, 10, 10, 12]))
print(highest_rank([12, 10, 8, 12, 7, 6, 4, 10, 10]))