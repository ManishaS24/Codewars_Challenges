
""" In this kata you are required to, given a string, replace every letter with its position in the alphabet.

If anything in the text isn't a letter, ignore it and don't return it.

"a" = 1, "b" = 2, etc.

Example
alphabet_position("The sunset sets at twelve o' clock.")
Should return "20 8 5 19 21 14 19 5 20 19 5 20 19 1 20 20 23 5 12 22 5 15 3 12 15 3 11" (as a string) """





from string import ascii_lowercase
test_text = "The sunset sets at twelve o' clock."

alphas = {letter: str(index) for index, letter in enumerate(ascii_lowercase, start=1)} 
# print(alphas)
def alphabet_position(text):
    text = text.lower()

    indx = [alphas[char] for char in text if char in alphas]

    return ' '.join(indx)
    

    

print(alphabet_position(test_text))