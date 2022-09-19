
import string

n = input()
s = input()

letters = {letter: s.count(letter) for letter in string.ascii_uppercase}.items()

left_part = ""
middle_letter = ""
middle_letter_not_find = True

for i in letters:
    number_of_letter = i[1]
    if number_of_letter == 0:
        continue
    else:
        letter = i[0]
        left_part += letter*int((number_of_letter//2))
        if middle_letter == "" and number_of_letter %2 != 0:
            middle_letter = letter



result = left_part + middle_letter + left_part[::-1]
print(result)
