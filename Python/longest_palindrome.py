# -*- coding: utf-8 -*-
"""
Created on Thu Dec  3 11:09:22 2020

@author: Manisha
"""

"""
Longest Palindrome
Find the length of the longest substring in the given string s that is the same in reverse.

As an example, if the input was “I like racecars that go fast”, the substring (racecar) length would be 7.

If the length of the input string is 0, the return value must be 0.

Example:
"a" -> 1 
"aab" -> 2  
"abcde" -> 1
"zzbaabcd" -> 4
"" -> 0
"""

# def longest_palindrome (s):
#     max_len = 0
#     pal_s = ""

   
#     for i in range(len(s)):
#         for j in range(i+1, len(s)+1):
#             new_s = s[i:j]
#             #print('new string', new_s)
#             if new_s == new_s[::-1]:
                
#                 if max_len > len(new_s):
#                     continue
#                 else:
#                     pal_s = new_s
#                     max_len = len(new_s)
            
            
#     return max_len, pal_s

def longest_palindrome (s):

    maxPal, tmpPal = 0, 1
    count_dct = {}
    inPal = False
                                               #zzbaabcd
    for i,l in enumerate(s):
        print('i,l:',i,l)
        count_dct[l] = count_dct.get(l,0) + 1
        print(count_dct)
        
        if not inPal and count_dct[l] >= 2:            # might encounter a palindrome, there...
            if l == s[i-1]:
                print('l first:', l)                          # ... palindrome with double character in the middle
                inPal = True
                tmpPal = 2
            
            elif l == s[i-2]: 
                print('l now:', l)                        # ... palindrome with one "peak" character in the middle
                inPal = True
                tmpPal = 3
        
        elif inPal and l == s[max(0, i-tmpPal-1)]:     # still in a palindrome...
                tmpPal += 2
            
        else:                                          # goes out of this palindrome
            inPal = False
            tmpPal = 1
        
        maxPal = max(maxPal, tmpPal)
    print(count_dct)
    return maxPal


  
            
        
  
#print(longest_palindrome("I like racecars that go fast"))
#print(longest_palindrome("a"))
print(longest_palindrome("zzbaabcd"))


