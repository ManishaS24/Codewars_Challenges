""" Implement the function unique_in_order which takes as argument a sequence and returns 
a list of items without any elements with the same value next to each other and preserving the original order of elements.

For example:

unique_in_order('AAAABBBCCDAABBB') == ['A', 'B', 'C', 'D', 'A', 'B']
unique_in_order('ABBCcAD')         == ['A', 'B', 'C', 'c', 'A', 'D']
unique_in_order([1,2,2,3,3])       == [1,2,3] """

# def unique_in_order(iterable):
#     l = list(iterable)
#     ud_list = []
    
#     for i in range(len(l)):
#         if len(ud_list) == 0:
#             ud_list.append(l[i])
#         if ud_list[-1] != l[i]:
#             ud_list.append(l[i])
        
#     # print(ud_list)
#     return(ud_list)

def unique_in_order(iterable):
    ud_list = []
    prev = None
    for ch in iterable[0:]:
        if ch != prev:
            ud_list.append(ch)
            prev = ch
    return ud_list

print(unique_in_order(['A']))
print(unique_in_order('ABBCcAD'))
print(unique_in_order('AAAABBBCCDAABBB'))
print(unique_in_order([1,2,2,3,3]))